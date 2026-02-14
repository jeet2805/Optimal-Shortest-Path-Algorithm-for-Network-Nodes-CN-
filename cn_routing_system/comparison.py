from dijkstra import dijkstra
from intelligent_routing import intelligent_routing

def compare_algorithms(graph, start, end):
    print("\nRouting Algorithm Performance Comparison\n")

    d_dist, d_path, d_hops = dijkstra(graph, start, end, 'distance')
    i_dist, i_path, i_hops = intelligent_routing(graph, start, end, 1,2,3)

    print("----------------------------------------------------")
    print("Metric        |  Dijkstra   |  Intelligent Routing")
    print("----------------------------------------------------")
    print(f"Total Weight  |   {d_dist:<10} |   {round(i_dist,2):<10}")
    print(f"Hop Count     |   {d_hops:<10} |   {i_hops:<10}")
    print("----------------------------------------------------")

    print("\nDijkstra Path:     ", " → ".join(d_path))
    print("Intelligent Path: ", " → ".join(i_path))
