from topology import default_topology
from dijkstra import dijkstra
from intelligent_routing import intelligent_routing
from simulation import reroute_after_congestion
from comparison import compare_algorithms

def main():
    net = default_topology()
    def validate_nodes(graph, s, d):
        if s not in graph or d not in graph:
            print("\n❌ Invalid node name! Valid nodes are:", list(graph.keys()))
            return False
        return True


    while True:
        print("\n==============================")
        print(" INTELLIGENT ROUTING SYSTEM ")
        print("==============================")
        print("1. Show Network Topology")
        print("2. Run Dijkstra Routing")
        print("3. Run Intelligent Routing")
        print("4. Simulate Congestion & Re-route")
        print("5. Compare Routing Algorithms")
        print("0. Exit")

        ch = input("\nEnter choice: ").strip()

        if ch == '1':
            net.display()

        elif ch == '2':
            s = input("Enter Source Node: ").upper().strip()
            d = input("Enter Destination Node: ").upper().strip()

            if not validate_nodes(net.graph, s, d):
                continue

            metric = input("Metric (distance/cost/delay): ").lower().strip()

            if metric not in ['distance', 'cost', 'delay']:
                print("\n❌ Invalid metric! Please choose from distance / cost / delay.")
                continue

            dist, path, hops = dijkstra(net.graph, s, d, metric)

            if dist is None:
                print("\n❌ ERROR: Invalid source or destination node!")
            else:
                print("\nDIJKSTRA ROUTING RESULT")
                print("Path:", " → ".join(path))
                print("Total:", dist)
                print("Hops:", hops)

        elif ch == '3':
            s = input("Enter Source Node: ").upper().strip()
            d = input("Enter Destination Node: ").upper().strip()

            if not validate_nodes(net.graph, s, d):
                continue

            print("Enter weight factors (α β γ)")
            try:
                alpha = float(input("α (distance weight): "))
                beta  = float(input("β (cost weight): "))
                gamma = float(input("γ (delay weight): "))
            except ValueError:
                print("\n❌ Invalid input! Please enter numeric values only.")
                continue

            dist, path, hops = intelligent_routing(net.graph, s, d, alpha, beta, gamma)

            if dist is None:
                print("\n❌ ERROR: Invalid source or destination node!")
            else:
                print("\nINTELLIGENT ROUTING RESULT")
                print("Path:", " → ".join(path))
                print("Total Weight:", round(dist,2))
                print("Hops:", hops)

        elif ch == '4':
            s = input("Enter Source Node: ").upper().strip()
            d = input("Enter Destination Node: ").upper().strip()

            if not validate_nodes(net.graph, s, d):
                continue

            dist, path, hops = reroute_after_congestion(net, s, d, 1, 2, 3)

            if dist is None:
                print("\n❌ Invalid node input!")
                continue

            print("\nUPDATED ROUTE AFTER CONGESTION")
            print("Path:", " → ".join(path))
            print("Total Weight:", round(dist,2))
            print("Hops:", hops)

        elif ch == '5':
            s = input("Enter Source Node: ").upper().strip()
            d = input("Enter Destination Node: ").upper().strip()

            if not validate_nodes(net.graph, s, d):
                continue

            compare_algorithms(net.graph, s, d)

        elif ch == '0':
            print("\nExiting System...")
            break

        else:
            print("❌ Invalid Choice! Please enter 0–5 only.")

if __name__ == "__main__":
    main()
