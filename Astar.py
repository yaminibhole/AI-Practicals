import heapq

def astar(grid, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {cell: float('inf') for row in grid for cell in row if cell != 'W'}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current, None)
            return list(reversed(path))

        x, y = current

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (x + dx, y + dy)

            if neighbor not in g_score:
                continue

            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # No path found

def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

# Example usage:
grid = [
    ['S', '.', '.', 'W'],
    ['.', 'W', '.', '.'],
    ['.', 'W', '.', 'W'],
    ['.', '.', '.', 'E']
]

start = (0, 0)
goal = (3, 3)

path = astar(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")
