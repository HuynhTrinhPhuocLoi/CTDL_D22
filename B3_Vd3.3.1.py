from collections import deque

class Queue:
    """
    Lớp triển khai hàng đợi (Queue) sử dụng deque.
    """

    def __init__(self):
        """
        Khởi tạo hàng đợi rỗng.
        """
        self.elements = deque()  # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        """
        Thêm một phần tử vào cuối hàng đợi.

        Args:
            item: Phần tử cần thêm vào.
        """
        self.elements.append(item)  # Thêm phần tử vào cuối deque
        print(f"Đã thêm '{item}' vào hàng đợi.")

    def dequeue(self):
        """
        Loại bỏ và trả về phần tử ở đầu hàng đợi.

        Returns:
            Phần tử ở đầu hàng đợi nếu hàng đợi không rỗng, ngược lại trả về None.
        """
        if not self.is_empty():
            item = self.elements.popleft()  # Loại bỏ phần tử ở đầu deque
            print(f"Đã lấy '{item}' ra khỏi hàng đợi.")
            return item
        else:
            print("Hàng đợi trống!")
            return None

    def front(self):
        """
        Trả về phần tử ở đầu hàng đợi mà không loại bỏ nó.

        Returns:
            Phần tử ở đầu hàng đợi nếu hàng đợi không rỗng, ngược lại trả về None.
        """
        if not self.is_empty():
            return self.elements[0]  # Truy cập phần tử đầu tiên
        else:
            print("Hàng đợi trống!")
            return None

    def is_empty(self):
        """
        Kiểm tra xem hàng đợi có rỗng hay không.

        Returns:
            True nếu hàng đợi rỗng, False nếu ngược lại.
        """
        return len(self.elements) == 0

    def size(self):
        """
        Trả về kích thước của hàng đợi.

        Returns:
            Số lượng phần tử trong hàng đợi.
        """
        return len(self.elements)

    def display(self):
        """
        In ra các phần tử trong hàng đợi từ đầu đến cuối.
        """
        print("Hàng đợi (đầu đến cuối):", list(self.elements))  # In hàng đợi từ đầu đến cuối

# Minh họa sử dụng hàng đợi
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue("Tài Liệu 1")
    queue.enqueue("Tài Liệu 2")
    queue.enqueue("Tài Liệu 3")

    queue.display()  # Output: Hàng đợi (đầu đến cuối): ['Tài Liệu 1', 'Tài Liệu 2', 'Tài Liệu 3']

    front_item = queue.front()
    if front_item is not None:
        print("Phần tử ở đầu hàng đợi:", front_item)  # Output: Tài Liệu 1

    queue.dequeue()
    queue.display()  # Output: Hàng đợi (đầu đến cuối): ['Tài Liệu 2', 'Tài Liệu 3']

    print("Hàng đợi có trống không?", queue.is_empty())  # Output: False

    queue.dequeue()
    queue.dequeue()
    print("Hàng đợi có trống không?", queue.is_empty()) #Output: True
    queue.dequeue() #Thử dequeue khi queue rỗng
    queue.front() #Thử front khi queue rỗng