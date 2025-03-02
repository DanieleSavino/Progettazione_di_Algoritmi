import os

def generate_header(lines: list[str]) -> str:
    if not lines[0].startswith('#'):
        return ''
    
    to_ret = lines[0].replace('#', '').strip()
    lines.pop(0)
    return to_ret

def generate_problem_description(lines: list[str]) -> str:
    md_lines = []

    i = 0
    first_found = None
    while i < len(lines):
        line = lines[i]
        if not line.startswith('"""'):
            i += 1
            continue

        if first_found is None:
            first_found = i
            i += 1
            continue

        break

    md_lines = [l.strip() for l in lines[first_found+1:i]]
    
    for _ in range(i+1):
        lines.pop(0)

    return "".join(md_lines)

def generate_approaches(lines: list[str]) -> list[str]:
    approaches = []

    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith('##'):
            approaches.append(lines[i].replace('##', '').strip())
            lines.pop(i)

    return approaches[::-1]

def generate_codes(lines: list[str]) -> list[str]:
    codes = []

    latest_def = None
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line.startswith('def'):
            if latest_def is None:
                latest_def = i
                continue

            codes.append([l for l in lines[latest_def:i]])
            latest_def = i
    
    codes.append(lines[latest_def:])

    for code in codes:
        for i in range(len(code)-1, -1, -1):
            line = code[i]
            if line == '\n':
                code.pop(i)
            else:
                break

    return codes

def generate_code_description(code: list[str]) -> list[str]:
    description = []

    first_found = None
    for i in range(len(code)-1, -1, -1):
        line = code[i].strip()
        if not line.startswith('"""'):
            continue

        if first_found is None:
            first_found = i
            continue

        description = [l.strip() for l in code[i+1:first_found]]

        del code[i:first_found+1]
        break

    return description

def generate_complexity(code: list[str]) -> dict[str, str]:
    complexity = {}

    for i in range(len(code)-1, -1, -1):
        line = code[i].strip()
        if line.startswith('# Tempo:'):
            complexity['time'] = line.replace('# Tempo:', '').strip()
            code.pop(i)
        elif line.startswith('# Spazio:'):
            complexity['space'] = line.replace('# Spazio:', '').strip()
            code.pop(i)

    return complexity

def generate_local_readme(lines: list[str]) -> str:
    header = generate_header(lines)
    problem_description = generate_problem_description(lines)

    approaches = generate_approaches(lines)
    codes = generate_codes(lines)

    codes_descriptions = []
    for code in codes:
        codes_descriptions.append(generate_code_description(code))

    complexities = []
    for code in codes:
        complexities.append(generate_complexity(code))

    md_lines = [f"# {header}", "", problem_description, ""]

    for i in range(len(approaches)):
        md_lines.append(f"{i+1}. [**{approaches[i]}**](#{i+1}-{"-".join(approaches[i].split(" ")).lower()})")

    md_lines.extend(["", "---", ""])
    
    for i, (approach, description, code, complexity) in enumerate(zip(approaches, codes_descriptions, codes, complexities)):
        md_lines.append(f"## {i+1}. {approach}")
        md_lines.append("")

        md_lines.append("### Descrizione:")
        md_lines.extend(description)
        md_lines.append("")

        md_lines.append("### Complessità:")
        md_lines.append(f"- **Tempo:** {complexity.get('time', 'N/A')}")
        md_lines.append(f"- **Spazio:** {complexity.get('space', 'N/A')}")
        md_lines.append("")

        md_lines.append("### Codice:")
        md_lines.append("```python")
        md_lines.append("".join(code))
        md_lines.append("```")

        md_lines.append("")
        if i >= len(approaches) - 1:
            break
        md_lines.append("---")
        md_lines.append("")

    return "\n".join(md_lines)

def local_readme_from_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        readme = generate_local_readme(f.readlines())

    out_path = file_path.replace('.py', '.md')
    with open(out_path, 'w') as f:
        f.write(readme)

    return out_path

def generate_rec(folder_path: str) -> list[str]:
    out_paths = []

    for file in os.listdir(folder_path):
        if file.endswith('.py'):
            out = local_readme_from_file(os.path.join(folder_path, file))
            out_paths.append(out)
        elif os.path.isdir(os.path.join(folder_path, file)):
            out_list = generate_rec(os.path.join(folder_path, file))
            out_paths.extend(out_list)

    return out_paths

def write_readme_template(template_path: str, readme_path: str, to_write: str) -> None:
    with open(template_path, 'r') as f:
        template = f.read()

    template = template % to_write

    with open(readme_path, 'w') as f:
        f.write(template)

def paths_sorter(x: str) -> int:
    folder_x = os.path.dirname(x)
    splitted_x = folder_x.split('_')

    if splitted_x[-1].isdecimal:
        return int(splitted_x[-1]), x
    
    return x

def get_folder_desrciption(path: str) -> str:
    desc_path = f'{path}/description.md'
    if not os.path.exists(desc_path):
        return ''

    with open(desc_path, 'r') as f:
        text = f.read()

    return text

def generate_main_readme_rec(from_path: list[str], template_path: str, readme_path: str) -> str:
    md_lines = []
    folders_map = {}

    out_paths = generate_rec(from_path)
    out_paths.sort(key=paths_sorter)

    for out_path in out_paths:
        folder = os.path.dirname(out_path)
        folder = folder.replace(from_path, '')
        folder = folder[1:]
        splitted = folder.split('_')
        folder = ' '.join([s.capitalize() for s in splitted])

        folders_map[folder] = folders_map.get(folder, []) + [out_path]


    for folder, out_paths in folders_map.items():
        description = get_folder_desrciption(os.path.dirname(out_paths[0]))
        md_lines.extend([f"## 📌 {folder}: {description}", "", "🔹 **Algoritmi trattati**:"])
        md_lines.extend([f"- ✅ [{' '.join(s.capitalize() for s in os.path.basename(out_path).replace('.md', '').split('_'))}]({out_path})" for out_path in out_paths])
        md_lines.extend(["", f"📂 **Percorso file:** `{os.path.dirname(out_paths[0])}`"])
        md_lines.extend(["", "---", ""])

    write_readme_template(template_path, readme_path, "\n".join(md_lines))

if __name__ == '__main__':
    generate_main_readme_rec('src', 'README_template.md', 'README.md')