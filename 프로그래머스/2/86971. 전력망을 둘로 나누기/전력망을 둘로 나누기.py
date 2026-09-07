def solution(n, wires):
    answer = n

    graph = [[] for _ in range(n+1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for cut_a, cut_b in wires:
        to_visit = [cut_a]
        visited = []

        while to_visit:
            current = to_visit.pop()
            visited.append(current)

            for next_node in graph[current]:
                if (current == cut_a and next_node == cut_b) or (current == cut_b and next_node == cut_a):
                    continue

                if next_node not in visited:
                    to_visit.append(next_node)

        diff = abs(len(visited) - (n - len(visited)))

        answer = min(answer, diff)

    return answer

    