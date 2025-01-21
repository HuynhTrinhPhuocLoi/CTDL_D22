from collections import deque

def dfs(grid, start, goal):
    """
    Tìm đường đi từ điểm bắt đầu (start) đến điểm đích (goal) trên lưới (grid) sử dụng DFS.

    Args:
        grid: Ma trận 2D biểu diễn lưới. 1 đại diện cho chướng ngại vật, 0 đại diện cho đường đi.
        start: Tuple (x, y) tọa độ điểm bắt đầu.
        goal: Tuple (x, y) tọa độ điểm đích.

    Returns:
        Một danh sách các tuple tọa độ tạo thành đường đi, hoặc None nếu không tìm thấy đường đi.
    """
    stack = deque([start])
    visited = set()
    parent = {}

    while stack:
        current = stack.pop()

        if current == goal:
            break

        if current in visited:
            continue

        visited.add(current)
        neighbors = get_neighbors(grid, current)

        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = current

    if goal not in parent and start != goal:
        print("Không tìm thấy đường đi.")
        return None

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent.get(current)  # Sử dụng .get() an toàn hơn
    path.append(start)
    path.reverse()
    return path

def get_neighbors(grid, position):
    """
    Lấy các vị trí lân cận hợp lệ của một vị trí trên lưới.

    Args:
        grid: Ma trận 2D biểu diễn lưới.
        position: Tuple (x, y) tọa độ của vị trí.

    Returns:
        Một danh sách các tuple tọa độ của các vị trí lân cận hợp lệ.
    """
    x, y = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lên, Xuống, Trái, Phải

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0: #Kết hợp điều kiện kiểm tra chướng ngại vật
            neighbors.append((nx, ny))
    return neighbors

if __name__ == "__main__":
    # 0: đường đi, 1: chướng ngại vật
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    path = dfs(grid, start, goal)

    if path:
        print("Đường đi tìm được:")
        print(path)
    else:
        print("Không tìm thấy đường đi.")

    grid2 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start2 = (0,0)
    goal2 = (2,2)
    path2 = dfs(grid2, start2, goal2)
    if path2:
        print("Đường đi tìm được:")
        print(path2)
    else:
        print("Không tìm thấy đường đi.")

    start3 = (0,0)
    goal3 = (0,0)
    path3 = dfs(grid2, start3, goal3)
    if path3:
        print("Đường đi tìm được:")
        print(path3)
    else:
        print("Không tìm thấy đường đi.")