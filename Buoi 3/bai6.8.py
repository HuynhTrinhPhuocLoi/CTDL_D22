def is_valid_number(k):

    digits = str(k)

    if all(int(digit) <= 5 for digit in digits) and len(digits) == len(set(digits)):
        return True
    return False

def count_valid_numbers(L, R):
    count = 0
    for k in range(L, R + 1):
        if is_valid_number(k):
            count += 1
    return count

def main():
    T = int(input()) 
    for _ in range(T):
        L, R = map(int, input().split())  
        print(count_valid_numbers(L, R))  

if __name__ == "__main__":
    main()
