def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    n, m = len(matrix), len(matrix[0])
    left, right = 0, n * m - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Convert mid index to 2D
        row = mid // m
        col = mid % m
        val = matrix[row][col]
        
        if val == target:
            return (row, col)
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None

mat = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

print(search_matrix(mat, 9))   # (1, 1)
print(search_matrix(mat, 6))   # None
