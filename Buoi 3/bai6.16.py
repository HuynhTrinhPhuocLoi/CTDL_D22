from collections import deque

def bfs(matrix, M, N):
    directions = [(0, 1), (1, 0)]
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = set()
    visited.add((0, 0))
    
    while queue:
        row, col, steps = queue.popleft()
        if row == M - 1 and col == N - 1:
            return steps
        for dr, dc in directions:
            new_row = row + dr * matrix[row][col]
            new_col = col + dc * matrix[row][col]
            if 0 <= new_row < M and 0 <= new_col < N and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))
    return -1

def main():
    T = int(input().strip())
    for _ in range(T):
        M, N = map(int, input().strip().split())
        matrix = []
        for _ in range(M):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        print(bfs(matrix, M, N))

if __name__ == "__main__":
    main()