def BFS_padri(G: list[list[int]], x: int):
    fathers_list = [-1] * len(G)
    fathers_list[x] = x

    i = 0
    queue = [x]
    while i < len(queue):
        father = queue[i]
        i += 1

        for node in G[father]:
            if fathers_list[node] != -1: continue

            fathers_list[node] = father
            queue.append(father)

    return fathers_list

def path_minimo(G: list[list[int]], x: int, t: int):
    fathers_list = BFS_padri(G, x)
    if fathers_list[t] == -1:
        return []
    
    path = [t]
    while fathers_list[t] != t:
        t = fathers_list[t]
        path.append(t)

    return path