function remove_parentheses(expression::String)::Vector{String}
    results = Set{String}()
    stack = []

    function remove_helper(expr::Vector{Char}, index::Int)
        if index > length(expr)
            push!(results, join(expr))
            return
        end

        if expr[index] == '('
            push!(stack, index)
            remove_helper(expr, index + 1)
            pop!(stack)
        elseif expr[index] == ')'
            if !isempty(stack)
                start = pop!(stack)
                expr[start] = ' '
                expr[index] = ' '
                remove_helper(expr, index + 1)
                expr[start] = '('
                expr[index] = ')'
                push!(stack, start)
            end
            remove_helper(expr, index + 1)
        else
            remove_helper(expr, index + 1)
        end
    end

    remove_helper(collect(expression), 1)
    return collect(results)
end

# Example usage
expression = readline(stdin)::String
results = remove_parentheses(expression)
for result in results
    println(result)
end