import Base: push!, pop!

mutable struct Stack
    elements::Vector{Any}
    Stack() = new(Vector{Any}())
end

function push!(s::Stack, item)
    push!(s.elements, item)
    println("Đã thêm '$item' vào ngăn xếp.")
end

function pop!(s::Stack)
    if isempty(s.elements)
        println("Ngăn xếp trống!")
        return nothing
    end
    item = pop!(s.elements)
    println("Đã lấy '$item' ra khỏi ngăn xếp.")
    return item
end

function peek(s::Stack)
    if isempty(s.elements)
        println("Ngăn xếp trống!")
        return nothing
    end
    return s.elements[end]
end

function is_empty(s::Stack)
    return isempty(s.elements)
end

function Base.display(s::Stack)
    println("Ngăn xếp (đỉnh đến đáy): ", reverse(s.elements))
end

function main()
    stack = Stack()
    push!(stack, "Sách A")
    push!(stack, "Sách B")
    push!(stack, "Sách C")

    display(stack)

    top_item = peek(stack)
    if top_item !== nothing
        println("Phần tử ở đỉnh ngăn xếp: ", top_item)
    end

    pop!(stack)
    display(stack)

    println("Ngăn xếp có trống không? ", is_empty(stack) ? "Có" : "Không")

    pop!(stack)
    pop!(stack)
    println("Ngăn xếp có trống không? ", is_empty(stack) ? "Có" : "Không")

    pop!(stack) # Kiểm tra pop khi stack rỗng
    peek(stack) # Kiểm tra peek khi stack rỗng
end

main()