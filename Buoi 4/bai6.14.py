from itertools import product

def generate_lucky_numbers(n):
    lucky_numbers = []
    for length in range(1, n + 1):
        for digits in product('68', repeat=length):
            lucky_numbers.append(''.join(digits))
    return sorted(lucky_numbers, reverse=True)

def main():
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        result = generate_lucky_numbers(N)
        print(len(result))
        print(' '.join(result))

if __name__ == "__main__":
    main()