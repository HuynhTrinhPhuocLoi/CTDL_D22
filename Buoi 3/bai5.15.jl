function next_smaller_of_next_larger(A::Vector{Int})::Vector{Int}
    n = length(A)
    next_larger = fill(-1, n)
    next_smaller = fill(-1, n)
    stack = []

    # Find the next larger element for each element
    for i in 1:n
        while !isempty(stack) && A[stack[end]] < A[i]
            next_larger[stack[end]] = i
            pop!(stack)
        end
        push!(stack, i)
    end

    # Find the next smaller element for the next larger element
    for i in 1:n
        if next_larger[i] != -1
            larger_index = next_larger[i]
            for j in larger_index+1:n
                if A[j] < A[larger_index]
                    next_smaller[i] = A[j]
                    break
                end
            end
        end
    end

    return next_smaller
end

# Example usage
A = [5, 1, 9, 2, 5, 1, 7]
println(next_smaller_of_next_larger(A))