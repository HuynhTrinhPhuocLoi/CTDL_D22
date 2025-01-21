def dfs(graph, start):
    """
    Duyệt đồ thị theo chiều sâu (DFS).

    Args:
        graph: Một từ điển (dictionary) biểu diễn đồ thị.
               Key là đỉnh (vertex), value là danh sách các đỉnh kề (neighbors).
        start: Đỉnh bắt đầu duyệt.
    """
    stack = [start]  # Khởi tạo stack với đỉnh bắt đầu
    visited = set()  # Tập hợp các đỉnh đã được thăm

    while stack:  # Lặp khi stack không rỗng
        vertex = stack.pop()  # Lấy đỉnh từ đỉnh stack (LIFO)

        if vertex not in visited:  # Kiểm tra nếu đỉnh chưa được thăm
            print(vertex, end=' ')  # In đỉnh
            visited.add(vertex)  # Đánh dấu đỉnh là đã thăm

            # Thêm các nút kề vào stack (đảo ngược để duyệt theo thứ tự)
            neighbors = list(reversed(graph[vertex])) #Chuyển neighbors thành list để in cho đẹp
            stack.extend(neighbors)  # Thêm các đỉnh kề vào stack
            print(f"Đã đẩy các nút kề của '{vertex}' vào ngăn xếp: {neighbors}")

    print()  # In xuống dòng sau khi duyệt xong

# Ví dụ sử dụng:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')

graph2 = {
    '0': ['1', '2'],
    '1': ['2'],
    '2': ['0', '3'],
    '3': ['3']
}

dfs(graph2, '2')