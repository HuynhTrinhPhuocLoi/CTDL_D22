function min_reversals_to_balance(expression::String)::Int
    # Length of the expression must be even to make it balanced by reversing
    if length(expression) % 2 != 0
        return -1  # Impossible to balance
    end

    stack = []
    for char in expression
        if char == '('
            push!(stack, char)
        else  # char == ')'
            if !isempty(stack) && stack[end] == '('
                pop!(stack)  # Found a matching pair
            else
                push!(stack, char)
            end
        end
    end

    # Stack now contains unbalanced parentheses
    unbalanced_open = unbalanced_close = 0
    while !isempty(stack)
        if pop!(stack) == '('
            unbalanced_open += 1
        else
            unbalanced_close += 1
        end
    end

    # It takes ceil(unbalanced_open / 2) + ceil(unbalanced_close / 2) reversals
    return div(unbalanced_open + 1, 2) + div(unbalanced_close + 1, 2)
end

# Example usage
expression = readline(stdin)::String
result = min_reversals_to_balance(expression)
if result == -1
    println("Impossible to balance")
else
    println("Minimum reversals needed: $result")
end