from collections import deque

def is_one_char_diff(s1, s2):

    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def bfs(s, t, words):

    queue = deque([(s, 0)])  
    visited = set([s])  
    
    while queue:
        current, steps = queue.popleft()
        

        if current == t:
            return steps
        
        for word in words:
            if word not in visited and is_one_char_diff(current, word):
                visited.add(word)
                queue.append((word, steps + 1))
    
    return -1  

def main():
    T = int(input())  
    for _ in range(T):
        
        n, s, t = input().split()  
        n = int(n)
        words = input().split()  

        print(bfs(s, t, words))

if __name__ == "__main__":
    main()
