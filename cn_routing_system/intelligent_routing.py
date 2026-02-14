import heapq

def intelligent_routing(graph, start, end, alpha=1, beta=1, gamma=1):

    if start not in graph or end not in graph:
        return None, [], 0

    pq = [(0, start, [])]
    visited = set()

    while pq:
        curr_weight, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == end:
            return curr_weight, path, len(path)-1

        for neighbor, metrics in graph[node].items():
            if neighbor not in visited:
                smart_weight = (
                    alpha * metrics['distance'] +
                    beta * metrics['cost'] +
                    gamma * metrics['delay']
                )
                heapq.heappush(
                    pq,
                    (curr_weight + smart_weight, neighbor, path)
                )

    return float('inf'), [], 0
