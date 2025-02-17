from collections import deque
import math

def min_operations(N):
    
    queue = deque([(N, 0)])
    visited = set([N])  

    while queue:
        current, steps = queue.popleft()

        if current == 1:
            return steps
        
        if current - 1 > 0 and (current - 1) not in visited:
            visited.add(current - 1)
            queue.append((current - 1, steps + 1))

        
        for i in range(2, int(math.sqrt(current)) + 1):
            if current % i == 0:
                u = i
                v = current // i
                if u > 1 and v > 1 and max(u, v) not in visited:
                    visited.add(max(u, v))
                    queue.append((max(u, v), steps + 1))

def main():
    T = int(input())  
    for _ in range(T):
        N = int(input())  
        print(min_operations(N))  

if __name__ == "__main__":
    main()
