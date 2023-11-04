def prim(graph):
    mst = []
    total_weight = 0
    visited = set()
    start_node = graph[0][0]

    visited.add(start_node)

    while len(visited) < len(set(node for edge in graph for node in edge[:2])):
        min_weight = float('inf')
        min_edge = None

        for u, v, weight in graph:
            if u in visited and v not in visited and weight < min_weight:
                min_weight = weight
                min_edge = (u, v, weight)
            elif v in visited and u not in visited and weight < min_weight:
                min_weight = weight
                min_edge = (u, v, weight)

        if min_edge:
            u, v, weight = min_edge
            visited.add(u)
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Example usage:
graph = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]

minimum_spanning_tree, total_weight = prim(graph)

print("Minimum Spanning Tree (edges and weights):")
for edge in minimum_spanning_tree:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")

print(f"Total weight of the Minimum Spanning Tree: {total_weight}")
