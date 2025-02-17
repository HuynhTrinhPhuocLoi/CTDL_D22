def is_bdn(number):
    
    return all(c in '01' for c in str(number))

def find_bdn(N):
    
    M = 1
    while True:
        P = M * N
        if is_bdn(P):
            return P
        M += 1

# Đọc số lượng test
T = int(input())

for _ in range(T):
    N = int(input())
    print(find_bdn(N))
