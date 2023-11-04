class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            x = min((dist[u], u) for u in range(self.V) if not sptSet[u])[1]
            sptSet[x] = True
            for y in range(self.V):
                if not sptSet[y] and self.graph[x][y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node, distance in enumerate(dist):
            print(node, "\t", distance)

if __name__ == "__main__":
    g = Graph(5)
    g.graph = [[0, 4, 0, 0, 0],
              [4, 0, 8, 0, 0],
              [0, 8, 0, 7, 0],
              [0, 0, 7, 0, 9],
              [0, 0, 0, 9, 0]
              ]

    g.dijkstra(0)
