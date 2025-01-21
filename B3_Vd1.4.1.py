import sys
sys.stdout.reconfigure(encoding='utf-8')

class Stack:
    def __init__(self):
        self.elements = []  # Sử dụng danh sách để lưu trữ các phần tử

    def push(self, item):
        self.elements.append(item)  # Thêm phần tử vào cuối danh sách
        print(f"Đã thêm '{item}' vào ngăn xếp.")

    def pop(self):
        if not self.is_empty():
            item = self.elements.pop()  # Loại bỏ phần tử cuối cùng
            print(f"Đã lấy '{item}' ra khỏi ngăn xếp.")
            return item
        else:
            print("Ngăn xếp trống!")
            return None

    def peek(self):
        if not self.is_empty():
            return self.elements[-1] # Truy cập phần tử cuối cùng
        else:
            print("Ngăn xếp trống!")
            return None

    def is_empty(self):
        return len(self.elements) == 0 # Kiểm tra xem danh sách có trống không

    def size(self):
        return len(self.elements) # Trả về kích thước ngăn xếp

    def display(self):
        print("Ngăn xếp (đỉnh đến đáy):", self.elements[::-1]) # In ngăn xếp từ đỉnh đến đáy

# Minh họa sử dụng ngăn xếp
if __name__ == "__main__":
    stack = Stack()
    stack.push("Sách A")
    stack.push("Sách B")
    stack.push("Sách C")

    stack.display() # Output: Ngăn xếp (đỉnh đến đáy): ['Sách C', 'Sách B', 'Sách A']

    top_item = stack.peek()
    if top_item: #Kiểm tra giá trị trả về có phải None không
        print("Phần tử ở đỉnh ngăn xếp:", top_item) # Output: Sách C

    stack.pop()
    stack.display() # Output: Ngăn xếp (đỉnh đến đáy): ['Sách B', 'Sách A']

    print("Ngăn xếp có trống không?", stack.is_empty()) # Output: False
    
    stack.pop()
    stack.pop()
    print("Ngăn xếp có trống không?", stack.is_empty()) # Output: True

    stack.pop() #Kiểm tra pop khi stack rỗng
    stack.peek() #Kiểm tra peek khi stack rỗng