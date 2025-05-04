import heapq

# Directions for moving in the grid (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm to find path
def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))  # (f_score, g_score, position)
    came_from = {}  # To reconstruct the path
    g_score = {start: 0}  # Cost from start to a node
    f_score = {start: heuristic(start, goal)}  # Estimated cost from start to goal through node

    while open_list:
        _, current_g_score, current = heapq.heappop(open_list)

        # If we've reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return path from start to goal

        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != "[]":
                tentative_g_score = current_g_score + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor))
                    came_from[neighbor] = current

    return None  # Return None if no path exists

# Define the grid (7x7)
grid_size = 7
grid = [["0" for _ in range(grid_size)] for _ in range(grid_size)]

# Mark obstacles on the grid ("[]" represents an obstacle)
obstacles = [(1, 5), (2, 4), (3, 4), (4, 3), (5, 3), (5, 2), (6, 2)]
for x, y in obstacles:
    grid[x][y] = "[]"

# Define start and end points
start = (1, 6)
end = (4, 2)

# Find the path using A*
path = astar(grid, start, end)

# Display the grid with the path
if path:
    print("Path found:", path)
   
    # Mark the path on the grid with '2'
    for x, y in path:
        if (x, y) != start:  # Don't overwrite the start point
            grid[x][y] = "2"  # 2 represents the path
   
    # Mark the start point as 'S'
    grid[start[0]][start[1]] = "S"
   
    # Print the grid
    for row in grid:
        print(" ".join(str(cell) for cell in row))
else:
    print("No path found")

