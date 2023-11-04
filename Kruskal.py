def kruskal(graph):
    graph.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = {node: node for node in set(node for edge in graph for node in edge[:2])}
    mst = []
    total_weight = 0

    for edge in graph:
        u, v, weight = edge
        if parent[u] != parent[v]:
            mst.append(edge)
            total_weight += weight
            old_parent = parent[u]
            new_parent = parent[v]
            for node, p in parent.items():
                if p == old_parent:
                    parent[node] = new_parent

    return mst, total_weight

# Example usage:
graph = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
minimum_spanning_tree, total_weight = kruskal(graph)

print("Minimum Spanning Tree (edges and weights):")
for edge in minimum_spanning_tree:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")

print(f"Total weight of the Minimum Spanning Tree: {total_weight}")
