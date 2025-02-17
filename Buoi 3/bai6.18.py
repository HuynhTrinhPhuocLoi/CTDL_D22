from collections import deque

# Hàm quay miếng ghép bên trái theo chiều kim đồng hồ
def rotate_left(state):
    new_state = state[:]
    new_state[0], new_state[1], new_state[3], new_state[4] = state[3], state[0], state[4], state[1]
    return new_state

# Hàm quay miếng ghép bên phải theo chiều kim đồng hồ
def rotate_right(state):
    new_state = state[:]
    new_state[1], new_state[2], new_state[4], new_state[5] = state[4], state[1], state[5], state[2]
    return new_state

# Hàm tìm số bước biến đổi ít nhất từ trạng thái ban đầu đến trạng thái đích
def min_transformations(start, target):
    queue = deque([(start, 0)])  # (trạng thái hiện tại, số bước)
    visited = set()
    visited.add(tuple(start))
    
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        # Quay miếng ghép bên trái
        left_rotated = rotate_left(current)
        if tuple(left_rotated) not in visited:
            visited.add(tuple(left_rotated))
            queue.append((left_rotated, steps + 1))
        # Quay miếng ghép bên phải
        right_rotated = rotate_right(current)
        if tuple(right_rotated) not in visited:
            visited.add(tuple(right_rotated))
            queue.append((right_rotated, steps + 1))
    return -1

def main():
    T = int(input().strip())
    for _ in range(T):
        start = list(map(int, input().strip().split()))
        target = list(map(int, input().strip().split()))
        print(min_transformations(start, target))

if __name__ == "__main__":
    main()