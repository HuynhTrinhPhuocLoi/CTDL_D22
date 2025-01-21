import Base: push!, popfirst!

mutable struct Queue
    elements::Vector{Any}
    Queue() = new(Vector{Any}())
end

function enqueue!(q::Queue, item)
    push!(q.elements, item)
    println("Đã thêm '$item' vào hàng đợi.")
end

function dequeue!(q::Queue)
    if isempty(q.elements)
        println("Hàng đợi trống!")
        return nothing
    end
    item = popfirst!(q.elements)
    println("Đã lấy '$item' ra khỏi hàng đợi.")
    return item
end

function front(q::Queue)
    if isempty(q.elements)
        println("Hàng đợi trống!")
        return nothing
    end
    return q.elements[1]
end

function is_empty(q::Queue)
    return isempty(q.elements)
end

function Base.display(q::Queue)
    println("Hàng đợi (đầu đến cuối): ", q.elements)
end

function main()
    queue = Queue()

    enqueue!(queue, "Tài Liệu 1")
    enqueue!(queue, "Tài Liệu 2")
    enqueue!(queue, "Tài Liệu 3")

    display(queue) # Output: Hàng đợi (đầu đến cuối): ["Tài Liệu 1", "Tài Liệu 2", "Tài Liệu 3"]

    front_item = front(queue)
    if front_item !== nothing #Kiểm tra giá trị trả về có phải nothing không
        println("Phần tử ở đầu hàng đợi: ", front_item) # Output: Phần tử ở đầu hàng đợi: Tài Liệu 1
    end

    dequeue!(queue)
    display(queue) # Output: Hàng đợi (đầu đến cuối): ["Tài Liệu 2", "Tài Liệu 3"]

    println("Hàng đợi có trống không? ", is_empty(queue) ? "Có" : "Không") # Output: Hàng đợi có trống không? Không

    dequeue!(queue)
    dequeue!(queue)
    println("Hàng đợi có trống không? ", is_empty(queue) ? "Có" : "Không") # Output: Hàng đợi có trống không? Có

    dequeue!(queue) #Kiểm tra dequeue khi queue rỗng
    front(queue) #Kiểm tra front khi queue rỗng
end

main()