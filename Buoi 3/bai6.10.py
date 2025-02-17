from collections import deque

def bfs(R, C, grid):
    queue = deque()

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_days = 0
    count_1 = 0  

    while queue:
        x, y, days = queue.popleft()
        

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:

                grid[nx][ny] = 2
                queue.append((nx, ny, days + 1))
                max_days = max(max_days, days + 1)
        

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                count_1 += 1
    
    if count_1 > 0:
        return -1
    return max_days

def main():
    T = int(input())  
    for _ in range(T):
        
        R, C = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(R)]
        
        
        result = bfs(R, C, grid)
        print(result)

if __name__ == "__main__":
    main()
