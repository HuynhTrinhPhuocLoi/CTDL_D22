function remove_parentheses(expression::String)::String
    stack = []
    result = []

    for char in expression
        if char == '('
            push!(stack, length(result))
        elseif char == ')'
            start = pop!(stack)
            if start > 0 && result[start - 1] in "+-"
                result[start - 1] = ""
            end
        else
            push!(result, char)
        end
    end

    return join(result)
end

# Example usage
T = parse(Int, readline(stdin))
for _ in 1:T
    exp = readline(stdin)
    println(remove_parentheses(exp))
end