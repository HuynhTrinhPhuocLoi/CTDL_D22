from collections import deque

# Chuyển đổi vị trí từ dạng "xy" sang tọa độ (x, y)
def position_to_coordinates(pos):
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1
    return (row, col)

# Kiểm tra xem tọa độ có nằm trong bàn cờ hay không
def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

# Tìm số bước di chuyển ít nhất của quân mã từ vị trí start đến vị trí end
def min_knight_moves(start, end):
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    start_pos = position_to_coordinates(start)
    end_pos = position_to_coordinates(end)
    
    queue = deque([(start_pos[0], start_pos[1], 0)])  # (row, col, steps)
    visited = set()
    visited.add(start_pos)
    
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == end_pos:
            return steps
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
    return -1

def main():
    T = int(input().strip())
    for _ in range(T):
        start, end = input().strip().split()
        print(min_knight_moves(start, end))

if __name__ == "__main__":
    main()