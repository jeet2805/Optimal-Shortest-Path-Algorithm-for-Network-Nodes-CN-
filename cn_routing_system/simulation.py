import random
import copy
from intelligent_routing import intelligent_routing

def simulate_congestion(network, congestion_factor=3):
    new_graph = copy.deepcopy(network.graph)

    print("\nSimulating Network Congestion...\n")

    for u in new_graph:
        for v in new_graph[u]:
            if random.random() < 0.3:
                old_delay = new_graph[u][v]['delay']
                new_graph[u][v]['delay'] *= congestion_factor
                print(f"Link {u} → {v} congested: Delay {old_delay}ms → {new_graph[u][v]['delay']}ms")

    return new_graph


def reroute_after_congestion(network, start, end, alpha=1, beta=1, gamma=1):
    print("\nRecalculating route after congestion...\n")

    new_graph = simulate_congestion(network)

    dist, path, hops = intelligent_routing(
        new_graph, start, end, alpha, beta, gamma
    )

    return dist, path, hops
