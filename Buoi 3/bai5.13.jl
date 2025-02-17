function is_operator(c::Char)::Bool
    return c in ['+', '-', '*', '/']
end

function precedence(op::Char)::Int
    if op in ['+', '-']
        return 1
    elseif op in ['*', '/']
        return 2
    else
        return 0
    end
end

function infix_to_postfix(expression::String)::Vector{String}
    output = []
    operators = []

    i = 1
    while i <= length(expression)
        char = expression[i]

        if isdigit(char)
            num = ""
            while i <= length(expression) && isdigit(expression[i])
                num *= expression[i]
                i += 1
            end
            push!(output, num)
            continue
        elseif char == '('
            push!(operators, char)
        elseif char == ')'
            while !isempty(operators) && operators[end] != '('
                push!(output, pop!(operators))
            end
            pop!(operators)  # Remove the '(' from the stack
        elseif is_operator(char)
            while !isempty(operators) && precedence(operators[end]) >= precedence(char)
                push!(output, pop!(operators))
            end
            push!(operators, char)
        end
        i += 1
    end

    while !isempty(operators)
        push!(output, pop!(operators))
    end

    return output
end

function apply_operator(op::Char, operand1::Int, operand2::Int)::Int
    if op == '+'
        return operand1 + operand2
    elseif op == '-'
        return operand1 - operand2
    elseif op == '*'
        return operand1 * operand2
    elseif op == '/'
        return div(operand1, operand2)
    else
        error("Unknown operator: $op")
    end
end

function evaluate_postfix(postfix::Vector{String})::Int
    stack = []

    for token in postfix
        if isdigit(token[1])
            push!(stack, parse(Int, token))
        else
            operand2 = pop!(stack)
            operand1 = pop!(stack)
            result = apply_operator(token[1], operand1, operand2)
            push!(stack, result)
        end
    end

    return stack[1]
end

function evaluate_infix(expression::String)::Int
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)
end

# Example usage
expression = readline(stdin)::String
println(evaluate_infix(expression))