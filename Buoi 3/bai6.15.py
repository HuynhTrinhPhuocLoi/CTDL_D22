from collections import deque

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_numbers():
    primes = []
    for i in range(1000, 10000):
        if is_prime(i):
            primes.append(i)
    return primes

def get_neighbors(num):
    neighbors = []
    num_str = str(num)
    for i in range(4):
        for digit in '0123456789':
            if digit != num_str[i]:
                new_num = int(num_str[:i] + digit + num_str[i+1:])
                if new_num >= 1000 and is_prime(new_num):
                    neighbors.append(new_num)
    return neighbors

def bfs(start, target):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    return -1

def main():
    T = int(input().strip())
    for _ in range(T):
        S, T = map(int, input().strip().split())
        print(bfs(S, T))

if __name__ == "__main__":
    main()