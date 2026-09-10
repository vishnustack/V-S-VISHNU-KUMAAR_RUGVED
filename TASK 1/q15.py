n = int(input("Enter the size n of the matrix: "))
matrix =[]
for i in range(n):
    # inputing values into the rows
    row = input(f"Enter row {i+1} ({n} numbers separated by spaces:) ").split()
    row = [int(x) for x in row]
    matrix.append(row)
for i in range(0, n - 1):
    for j in range(i + 1, n):
        # swapping numbers
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for row in matrix:
    row.reverse()
    # printing the rotated matrix
    print(row)
# initializing values
top, bottom, left, right = 0, n-1, 0, n-1
# initializing an empty list
result = []

# Loop for spiral order
while top <=bottom and left <= right:
    for col in range(left, right + 1):
        result.append(matrix[top][col])
    top += 1

    for row in range(top, bottom + 1):
        result.append(matrix[row][right])
    right -= 1

    if top <= bottom:
        for col in range(right, left - 1, -1):
            result.append(matrix[bottom][col])
        bottom -= 1

    if left <= right:
        for row in range(bottom, top - 1, - 1):
            result.append(matrix[row][left])
        left += 1

# printing the spiral list
print(result)