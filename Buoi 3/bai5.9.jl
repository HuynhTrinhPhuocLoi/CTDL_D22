function is_operator(c::Char)::Bool
    return c in ['+', '-', '*', '/', '^']
end

function postfix_to_prefix(expression::String)::String
    stack = []

    # Iterate over the expression from left to right
    for char in expression
        if is_operator(char)
            # Pop two operands from the stack
            operand2 = pop!(stack)
            operand1 = pop!(stack)

            # Combine them into a single string with the operator at the beginning
            new_expr = "$char $operand1 $operand2"

            # Push the resulting expression back onto the stack
            push!(stack, new_expr)
        else
            # Push the operand onto the stack
            push!(stack, string(char))
        end
    end

    # The final element on the stack is the complete prefix expression
    return stack[1]
end

# Example usage
expression = readline(stdin)::String
println(postfix_to_prefix(expression))