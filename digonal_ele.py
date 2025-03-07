def diagonal_sum(matrix, level=1):
    n = len(matrix)
    primary_sum = sum(matrix[i][i] for i in range(n))  
    
    if level == 1:
        return primary_sum 
    
    secondary_sum = sum(matrix[i][n-i-1] for i in range(n))  
    if n % 2 == 1:  
        secondary_sum -= matrix[n//2][n//2]
    
    return primary_sum + secondary_sum  


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Level 1 Diagonal Sum:", diagonal_sum(matrix, level=1))  
print("Level 2 Diagonal Sum:", diagonal_sum(matrix, level=2))  
