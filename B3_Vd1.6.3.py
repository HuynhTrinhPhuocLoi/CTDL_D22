def decimal_to_binary(n):
    """Chuyển đổi số thập phân n sang nhị phân.

    Args:
        n: Số thập phân cần chuyển đổi (phải là số nguyên không âm).

    Returns:
        Chuỗi biểu diễn số nhị phân, hoặc None nếu n là số âm.
        Gây ra TypeError nếu n không phải là số nguyên.
    """

    if not isinstance(n, int):
        raise TypeError("Đầu vào phải là một số nguyên.")

    if n < 0:
        print("Số thập phân phải là số không âm.")
        return None

    if n == 0:
        return "0"

    stack = []
    print(f"Chuyển đổi số thập phân: {n} sang nhị phân.")  # In thông báo ban đầu

    while n > 0:
        remainder = n % 2
        stack.append(remainder)
        print(f"Chia {n} cho 2, phần dư: {remainder} — Đẩy {remainder} vào ngăn xếp.")
        n //= 2  # Tương đương với n = n // 2 (chia lấy phần nguyên)
        print(f"Thương mới: {n}")

    binary = ""
    print("Chuyển đổi ngăn xếp thành số nhị phân:")

    while stack:
        binary += str(stack.pop())
        print(f"Lấy {binary[-1]} từ ngăn xếp và nối vào kết quả.")

    return binary

# Minh họa
number = 13
binary = decimal_to_binary(number)
if binary is not None:
    print(f"Số thập phân {number} chuyển sang nhị phân là: {binary}")  # Output: 1101

number = 0
binary = decimal_to_binary(number)
if binary is not None:
    print(f"Số thập phân {number} chuyển sang nhị phân là: {binary}")  # Output: 0

number = 25
binary = decimal_to_binary(number)
if binary is not None:
    print(f"Số thập phân {number} chuyển sang nhị phân là: {binary}")  # Output: 11001

number = -5  # Kiểm tra số âm
binary = decimal_to_binary(number)
if binary is not None:
    print(f"Số thập phân {number} chuyển sang nhị phân là: {binary}")

try:
    number = "abc"  # Kiểm tra kiểu dữ liệu
    binary = decimal_to_binary(number)
    if binary is not None:
        print(f"Số thập phân {number} chuyển sang nhị phân là: {binary}")
except TypeError as e:
    print(f"Lỗi: {e}")