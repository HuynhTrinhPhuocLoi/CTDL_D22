from collections import deque

class RequestQueue:
    """
    Lớp quản lý hàng đợi yêu cầu.
    """

    def __init__(self):
        """
        Khởi tạo hàng đợi rỗng.
        """
        self.queue = deque()

    def add_request(self, request):
        """
        Thêm một yêu cầu vào hàng đợi.

        Args:
            request: Yêu cầu cần thêm vào (thường là một chuỗi).
        """
        self.queue.append(request)
        print(f"Đã thêm yêu cầu '{request}' vào hàng đợi.")

    def process_request(self):
        """
        Xử lý yêu cầu ở đầu hàng đợi.
        """
        if self.queue:  # Kiểm tra nếu hàng đợi không rỗng (Pythonic way)
            request = self.queue.popleft()
            print(f"Đang xử lý yêu cầu: '{request}'")
            # Thực hiện xử lý yêu cầu ở đây (ví dụ: gọi một hàm xử lý)
        else:
            print("Không có yêu cầu nào để xử lý.")

    def display_queue(self):
        """
        Hiển thị nội dung của hàng đợi.
        """
        print("Hàng đợi yêu cầu:", list(self.queue))

# Minh họa sử dụng hàng đợi yêu cầu
if __name__ == "__main__":
    rq = RequestQueue()

    rq.add_request("Yêu Cầu 1")
    rq.add_request("Yêu Cầu 2")
    rq.add_request("Yêu Cầu 3")

    rq.display_queue()
    # Output: Hàng đợi yêu cầu: ['Yêu Cầu 1', 'Yêu Cầu 2', 'Yêu Cầu 3']

    rq.process_request()
    rq.display_queue()
    # Output: Đang xử lý yêu cầu: 'Yêu Cầu 1'
    #         Hàng đợi yêu cầu: ['Yêu Cầu 2', 'Yêu Cầu 3']

    rq.process_request()
    rq.display_queue()
    # Output: Đang xử lý yêu cầu: 'Yêu Cầu 2'
    #         Hàng đợi yêu cầu: ['Yêu Cầu 3']

    rq.process_request()
    rq.display_queue()
    # Output: Đang xử lý yêu cầu: 'Yêu Cầu 3'
    #         Hàng đợi yêu cầu: []

    rq.process_request()
    # Output: Không có yêu cầu nào để xử lý.