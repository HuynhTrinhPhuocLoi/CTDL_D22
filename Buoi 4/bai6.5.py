from collections import deque

def min_operations(S, T):
    # Queue chứa (số hiện tại, số bước)
    queue = deque([(S, 0)])
    # Set để kiểm tra số đã thăm
    visited = set()
    visited.add(S)

    while queue:
        current, steps = queue.popleft()

        if current == T:
            return steps

        
        if current - 1 >= 0 and (current - 1) not in visited:
            visited.add(current - 1)
            queue.append((current - 1, steps + 1))

        
        if current * 2 <= 10000 and (current * 2) not in visited:
            visited.add(current * 2)
            queue.append((current * 2, steps + 1))

def main():
    T = int(input())  
    for _ in range(T):
        S, T = map(int, input().split())  
        print(min_operations(S, T))  

if __name__ == "__main__":
    main()
