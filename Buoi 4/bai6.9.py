from collections import deque

def is_clear_path(board, x1, y1, x2, y2):
    if x1 == x2:  # Cùng hàng
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):  
            if board[x1][y] == 'X':
                return False
        return True
    if y1 == y2:  # Cùng cột
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x): 
            if board[x][y1] == 'X':
                return False
        return True
    return False

def bfs(board, start, end, N):
    queue = deque([(start[0], start[1], 0)])  
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == end:
            return steps
        

        for ny in range(N):
            if ny != y and not visited[x][ny] and board[x][ny] == '.':
                if is_clear_path(board, x, y, x, ny):
                    visited[x][ny] = True
                    queue.append((x, ny, steps + 1))

        for nx in range(N):
            if nx != x and not visited[nx][y] and board[nx][y] == '.':
                if is_clear_path(board, x, y, nx, y):
                    visited[nx][y] = True
                    queue.append((nx, y, steps + 1))
    
    return -1  

def main():
    T = int(input())  
    for _ in range(T):
        N = int(input())  
        board = [input().strip() for _ in range(N)]
        a, b, c, d = map(int, input().split()) 
        
        result = bfs(board, (a, b), (c, d), N)
        print(result)

if __name__ == "__main__":
    main()
