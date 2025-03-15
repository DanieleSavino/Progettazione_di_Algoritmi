def BFS(G: list[list[int]], x: int) -> list[bool]:
    seen = [False] * len(G)
    seen[x] = True

    i = 0
    queue = [x]
    while i < len(queue):
        father = queue[i]
        i += 1

        for node in G[father]:
            if seen[node]: continue

            seen[node] = True
            queue.append(node)

    return seen