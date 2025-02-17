from collections import deque

# Hàm thực hiện BFS
def bfs(A, B, C, grid, start, end):
    # Các hướng di chuyển trong không gian 3 chiều (trái, phải, trên, dưới, trước, sau)
    directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    
    # Khởi tạo hàng đợi với điểm xuất phát
    queue = deque([(start[0], start[1], start[2], 0)])  # (x, y, z, bước đi)
    
    # Đánh dấu các ô đã thăm
    visited = [[[False] * C for _ in range(B)] for _ in range(A)]
    visited[start[0]][start[1]][start[2]] = True
    
    while queue:
        x, y, z, steps = queue.popleft()
        
        # Nếu đến điểm đích
        if (x, y, z) == end:
            return steps
        
        # Duyệt các hướng di chuyển
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            
            # Kiểm tra xem tọa độ có hợp lệ không
            if 0 <= nx < A and 0 <= ny < B and 0 <= nz < C:
                # Nếu ô chưa thăm và không phải vật cản
                if not visited[nx][ny][nz] and grid[nx][ny][nz] != '#':
                    visited[nx][ny][nz] = True
                    queue.append((nx, ny, nz, steps + 1))
    
    # Nếu không tìm được đường đi
    return -1

def main():
    T = int(input())  # Số lượng test
    for _ in range(T):
        # Đọc kích thước của hình hộp
        A, B, C = map(int, input().split())
        
        # Đọc vào các lát cắt của hình hộp
        grid = []
        start = end = None
        for i in range(A):
            layer = []
            for j in range(B):
                row = input().strip()
                if 'S' in row:
                    start = (i, j, row.index('S'))
                if 'E' in row:
                    end = (i, j, row.index('E'))
                layer.append(row)
            grid.append(layer)
        
        # Tính toán và in kết quả cho mỗi test
        result = bfs(A, B, C, grid, start, end)
        print(result)

if __name__ == "__main__":
    main()
