def count_bdn(N):
    # Tạo danh sách các số BDN bằng cách sinh từ nhỏ đến lớn
    queue = ['1']
    count = 0
    
    while queue:
        current = queue[0]
        queue.pop(0)
        
        # Nếu số hiện tại nhỏ hơn N thì tăng đếm
        if int(current) < N:
            count += 1
            # Thêm 2 số tiếp theo bằng cách thêm 0 và 1 vào cuối
            queue.append(current + '0')
            queue.append(current + '1')
        else:
            break
            
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_bdn(N))