#SO Nhi phan tu 1 den N
def binary_numbers(n):
    """
    Chuyển đổi các số từ 1 đến n thành dạng nhị phân
    Args:
        n (int): Số nguyên dương
    Returns:
        str: Chuỗi các số nhị phân cách nhau bởi khoảng trắng
    """
    result = []
    for i in range(1, n + 1):
        result.append(bin(i)[2:])
    return " ".join(result)

def main():
    try:
        T = int(input())  # Số test case
        for _ in range(T):
            n = int(input())
            if n <= 0:
                print("Vui lòng nhập số nguyên dương")
                continue
            print(binary_numbers(n))
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ")

if __name__ == "__main__":
    main()