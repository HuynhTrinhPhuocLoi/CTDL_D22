def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    
    # Create a matrix to store distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the matrix
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Compute the Levenshtein distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                           dp[i][j - 1] + 1,      # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution
    
    return dp[m][n]

# Example usage
s = "kitten"
t = "sitting"
print(f"The Levenshtein distance between '{s}' and '{t}' is {levenshtein_distance(s, t)}")