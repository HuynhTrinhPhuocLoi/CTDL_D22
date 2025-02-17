function smallest_number_from_pattern(S::String)::String
    n = length(S)
    result = []
    stack = []

    for i in 1:n+1
        push!(stack, i)
        if i == n+1 || S[i] == 'I'
            while !isempty(stack)
                push!(result, pop!(stack))
            end
        end
    end

    return join(result)
end

# Example usage
S = readline(stdin)::String
println(smallest_number_from_pattern(S))