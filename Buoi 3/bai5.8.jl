function is_operator(c::Char)::Bool
    return c in ['+', '-', '*', '/', '^']
end

function prefix_to_postfix(expression::String)::String
    stack = []

    # Iterate over the expression from right to left
    for i in reverse(1:length(expression))
        char = expression[i]

        if is_operator(char)
            # Pop two operands from the stack
            operand1 = pop!(stack)
            operand2 = pop!(stack)

            # Combine them into a single string with the operator at the end
            new_expr = "$operand1 $operand2 $char"

            # Push the resulting expression back onto the stack
            push!(stack, new_expr)
        else
            # Push the operand onto the stack
            push!(stack, string(char))
        end
    end

    # The final element on the stack is the complete postfix expression
    return stack[1]
end

# Example usage
expression = readline(stdin)::String
println(prefix_to_postfix(expression))