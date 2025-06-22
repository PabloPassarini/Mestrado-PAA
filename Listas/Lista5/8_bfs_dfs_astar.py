import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import time
from collections import deque
import heapq

# Visualização
def show_maze(maze, path=None, visited=None, delay=0.2):
    color_map = {
        '0': 1,  # branco
        '1': 0,  # preto
        's': 0.5,  # cinza
        'g': 0.75  # cinza claro
    }

    m, n = len(maze), len(maze[0])
    grid = [[color_map.get(cell, 1) for cell in row] for row in maze]

    fig, ax = plt.subplots()
    cmap = mcolors.ListedColormap(['black', 'white', 'gray', 'lightgray', 'blue', 'red'])

    for i in range(m):
        for j in range(n):
            if visited and (i, j) in visited:
                grid[i][j] = 4  # azul para visitado
            if path and (i, j) in path:
                grid[i][j] = 5  # vermelho para caminho final

    ax.imshow(grid, cmap=cmap)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.draw()
    plt.pause(delay)
    plt.clf()

# Funções auxiliares
def parse_maze(maze):
    start = goal = None
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 's':
                start = (i, j)
            elif val == 'g':
                goal = (i, j)
    return start, goal

def get_neighbors(pos, maze):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    m, n = len(maze), len(maze[0])
    for dx, dy in directions:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != '1':
            yield (nx, ny)

def reconstruct_path(came_from, end):
    path = []
    while end:
        path.append(end)
        end = came_from.get(end)
    return path[::-1]

# DFS com visualização
def dfs(maze):
    start, goal = parse_maze(maze)
    stack = [start]
    came_from = {start: None}
    visited = set()

    while stack:
        current = stack.pop()
        if current == goal:
            show_maze(maze, reconstruct_path(came_from, current), visited)
            return reconstruct_path(came_from, current)
        visited.add(current)
        show_maze(maze, None, visited)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited and neighbor not in stack:
                came_from[neighbor] = current
                stack.append(neighbor)
    return None

# BFS com visualização
def bfs(maze):
    start, goal = parse_maze(maze)
    queue = deque([start])
    came_from = {start: None}
    visited = set()

    while queue:
        current = queue.popleft()
        if current == goal:
            show_maze(maze, reconstruct_path(came_from, current), visited)
            return reconstruct_path(came_from, current)
        visited.add(current)
        show_maze(maze, None, visited)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited and neighbor not in queue:
                came_from[neighbor] = current
                queue.append(neighbor)
    return None

# A* com visualização
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze):
    start, goal = parse_maze(maze)
    open_set = [(0 + heuristic(start, goal), 0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = set()

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        if current == goal:
            show_maze(maze, reconstruct_path(came_from, current), visited)
            return reconstruct_path(came_from, current)

        visited.add(current)
        show_maze(maze, None, visited)

        for neighbor in get_neighbors(current, maze):
            new_cost = cost + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    return None

# Exemplo de uso
maze = [
    ['s', '0', '1', '0', 'g'],
    ['1', '0', '1', '0', '1'],
    ['0', '0', '0', '0', '0'],
]

print("DFS Path:", dfs(maze))
time.sleep(1)
print("BFS Path:", bfs(maze))
time.sleep(1)
print("A* Path:", astar(maze))
plt.close()
