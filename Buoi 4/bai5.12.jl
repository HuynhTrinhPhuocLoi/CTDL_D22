function is_operator(c::Char)::Bool
    return c in ['+', '-', '*', '/', '^']
end

function apply_operator(op::Char, operand1::Float64, operand2::Float64)::Float64
    if op == '+'
        return operand1 + operand2
    elseif op == '-'
        return operand1 - operand2
    elseif op == '*'
        return operand1 * operand2
    elseif op == '/'
        return operand1 / operand2
    elseif op == '^'
        return operand1 ^ operand2
    else
        error("Unknown operator: $op")
    end
end

function evaluate_prefix(expression::String)::Float64
    stack = []

    # Iterate over the expression from right to left
    for i in reverse(1:length(expression))
        char = expression[i]

        if is_operator(char)
            # Pop two operands from the stack
            operand1 = pop!(stack)
            operand2 = pop!(stack)

            # Apply the operator and push the result back onto the stack
            result = apply_operator(char, operand1, operand2)
            push!(stack, result)
        else
            # Push the operand onto the stack
            push!(stack, parse(Float64, string(char)))
        end
    end

    # The final element on the stack is the result of the expression
    return stack[1]
end

# Example usage
expression = readline(stdin)::String
println(evaluate_prefix(expression))