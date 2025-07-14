from collections import deque
import heapq

class MazeSolver:
    """
    Classe para resolver um labirinto usando DFS, BFS e A*.
    """
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start_pos = self._find_char('s')
        self.goal_pos = self._find_char('g')

    def _find_char(self, char):
        """Encontra as coordenadas de um caractere no labirinto."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == char:
                    return (r, c)
        return None

    def get_neighbors(self, pos):
        """Retorna uma lista de vizinhos válidos (não são paredes e estão dentro dos limites)."""
        r, c = pos
        neighbors = []
        # Movimentos possíveis: cima, baixo, esquerda, direita
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.maze[nr][nc] != 1:
                neighbors.append((nr, nc))
        return neighbors

    def _reconstruct_path(self, came_from, current):
        """Reconstrói o caminho do início ao fim a partir do dicionário 'came_from'."""
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(self.start_pos)
        return path[::-1] # Retorna o caminho na ordem correta (início -> fim)

    def solve_dfs(self):
        """Resolve o labirinto usando Busca em Profundidade (DFS)."""
        stack = [self.start_pos]
        visited = {self.start_pos}
        came_from = {}

        while stack:
            current = stack.pop()

            if current == self.goal_pos:
                return self._reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    stack.append(neighbor)
        
        return None # Caminho não encontrado

    def solve_bfs(self):
        """Resolve o labirinto usando Busca em Largura (BFS)."""
        queue = deque([self.start_pos])
        visited = {self.start_pos}
        came_from = {}

        while queue:
            current = queue.popleft()

            if current == self.goal_pos:
                return self._reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    queue.append(neighbor)
        
        return None # Caminho não encontrado

    def _manhattan_distance(self, pos1, pos2):
        """Calcula a heurística da Distância de Manhattan."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def solve_a_star(self):
        """Resolve o labirinto usando o algoritmo A* (A-Estrela)."""
        # Fila de prioridade: (f_score, g_score, posição)
        # g_score é usado como desempate para garantir consistência
        open_set = [(self._manhattan_distance(self.start_pos, self.goal_pos), 0, self.start_pos)]
        
        came_from = {}
        g_score = { (r, c): float('inf') for r in range(self.rows) for c in range(self.cols) }
        g_score[self.start_pos] = 0

        while open_set:
            _, g, current = heapq.heappop(open_set)

            if current == self.goal_pos:
                return self._reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1 # Custo do movimento é sempre 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self._manhattan_distance(neighbor, self.goal_pos)
                    heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))

        return None # Caminho não encontrado

    def print_solution(self, path, algorithm_name):
        """Imprime o labirinto com o caminho da solução."""
        print(f"--- Solução encontrada por: {algorithm_name} ---")
        if path is None:
            print("Nenhum caminho foi encontrado.")
            return

        print(f"Comprimento do caminho: {len(path) - 1} passos")
        
        # Cria uma cópia do labirinto para desenhar o caminho
        solved_maze = [list(row) for row in self.maze]
        for pos in path:
            if pos != self.start_pos and pos != self.goal_pos:
                r, c = pos
                solved_maze[r][c] = '*' # Marca o caminho com '*'
        
        for row in solved_maze:
            print(" ".join(map(str, row)))
        print("-" * (len(self.maze[0]) * 2 -1))

# --- Execução Principal ---
if __name__ == "__main__":
    # Definição do labirinto
    # 0: caminho livre, 1: parede, 's': início, 'g': fim
    labirinto_exemplo = [
        ['s', 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 'g']
    ]

    solver = MazeSolver(labirinto_exemplo)

    # Resolvendo com DFS
    path_dfs = solver.solve_dfs()
    solver.print_solution(path_dfs, "DFS")

    # Resolvendo com BFS
    path_bfs = solver.solve_bfs()
    solver.print_solution(path_bfs, "BFS")
    
    # Resolvendo com A*
    path_a_star = solver.solve_a_star()
    solver.print_solution(path_a_star, "A*")