def bfs(graph, start):
    """
    Duyệt đồ thị theo chiều rộng (BFS).

    Args:
        graph: Một từ điển (dictionary) biểu diễn đồ thị.
               Key là đỉnh (vertex), value là danh sách các đỉnh kề (neighbors).
        start: Đỉnh bắt đầu duyệt.
    """
    queue = [start]  # Khởi tạo hàng đợi với đỉnh bắt đầu
    visited = set()  # Tập hợp các đỉnh đã được thăm

    while queue:  # Lặp khi hàng đợi không rỗng
        vertex = queue.pop(0)  # Lấy đỉnh từ đầu hàng đợi (FIFO)

        if vertex not in visited:  # Kiểm tra nếu đỉnh chưa được thăm
            print(vertex, end=' ')  # In đỉnh
            visited.add(vertex)  # Đánh dấu đỉnh là đã thăm

            # Thêm các nút kề chưa được thăm vào cuối hàng đợi
            neighbors = graph[vertex]
            queue.extend(neighbors)  # Thêm các đỉnh kề vào hàng đợi
            print(f"Đã thêm các nút kề của '{vertex}' vào hàng đợi: {neighbors}") #In thông tin các nút kề được thêm vào

    print()  # In xuống dòng sau khi duyệt xong

# Minh họa
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS từ nút A:")
bfs(graph, 'A')  # Output: A B C D E F

graph2 = {
    '0': ['1', '2'],
    '1': ['2'],
    '2': ['0', '3'],
    '3': ['3']
}

print("\nBFS từ nút 2:")
bfs(graph2, '2')