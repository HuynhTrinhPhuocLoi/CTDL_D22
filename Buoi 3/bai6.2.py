from collections import deque

def smallest_multiple_of_n(n):
    queue = deque(["9"])
    while queue:
        num = queue.popleft()
        if int(num) % n == 0:  
            return num
        queue.append(num + "0")  
        queue.append(num + "9")  

def main():
    T = int(input())  
    for _ in range(T):
        n = int(input())  
        print(smallest_multiple_of_n(n))  

if __name__ == "__main__":
    main()
