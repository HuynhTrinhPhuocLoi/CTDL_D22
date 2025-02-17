function are_expressions_equal(P1::String, P2::String)::Bool
    return P1 == P2
end

# Example usage
P1 = readline(stdin)::String
P2 = readline(stdin)::String

if are_expressions_equal(P1, P2)
    println("The expressions are equal.")
else
    println("The expressions are not equal.")
end