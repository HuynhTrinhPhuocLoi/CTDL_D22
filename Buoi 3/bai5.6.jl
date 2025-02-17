function infix_to_postfix(expression::String)::String
    precedence = Dict(
        '+' => 1,
        '-' => 1,
        '*' => 2,
        '/' => 2,
        '^' => 3
    )
    is_left_associative = Dict(
        '+' => true,
        '-' => true,
        '*' => true,
        '/' => true,
        '^' => false
    )

    output = []
    operators = []

    for char in expression
        if isletter(char) || isdigit(char)
            push!(output, char)
        elseif char == '('
            push!(operators, char)
        elseif char == ')'
            while !isempty(operators) && operators[end] != '('
                push!(output, pop!(operators))
            end
            if !isempty(operators) && operators[end] == '('
                pop!(operators)
            end
        else
            while !isempty(operators) && operators[end] != '(' &&
                  (precedence[operators[end]] > precedence[char] ||
                  (precedence[operators[end]] == precedence[char] && is_left_associative[char]))
                push!(output, pop!(operators))
            end
            push!(operators, char)
        end
    end

    while !isempty(operators)
        push!(output, pop!(operators))
    end

    return join(output)
end

# Example usage
expression = readline(stdin)::String
println(infix_to_postfix(expression))