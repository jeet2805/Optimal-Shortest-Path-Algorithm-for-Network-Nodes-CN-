import random

class NetworkGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, u, v, distance, cost, delay):
        self.add_node(u)
        self.add_node(v)

        self.graph[u][v] = {
            'distance': distance,
            'cost': cost,
            'delay': delay
        }

        self.graph[v][u] = {
            'distance': distance,
            'cost': cost,
            'delay': delay
        }

    def display(self):
        print("\nNetwork Topology:\n")
        for u in self.graph:
            for v in self.graph[u]:
                print(f"{u} → {v} | Distance={self.graph[u][v]['distance']} | "
                      f"Cost={self.graph[u][v]['cost']} | Delay={self.graph[u][v]['delay']}ms")
        print()


def default_topology():
    net = NetworkGraph()

    edges = [
        ('A','B',4,5,10),
        ('A','C',2,3,15),
        ('B','C',1,2,5),
        ('B','D',7,6,20),
        ('C','D',3,4,8),
        ('C','E',6,7,12),
        ('D','E',2,3,6),
        ('D','F',5,6,18),
        ('E','F',3,4,10)
    ]

    for u,v,d,c,dl in edges:
        net.add_edge(u,v,d,c,dl)

    return net


def random_topology(n=10):
    net = NetworkGraph()
    nodes = [chr(65+i) for i in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if random.random() < 0.4:
                d = random.randint(1,10)
                c = random.randint(1,10)
                dl = random.randint(5,25)
                net.add_edge(nodes[i], nodes[j], d, c, dl)

    return net
