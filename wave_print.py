def wave_print(matrix, m, n):
    ans = []
    for cols in range(0, n):
        if cols % 2 == 0:
            for rows in range(0, m):  # m should be the row count, not n
                ans.append(matrix[rows][cols])
        else:
            for rows in range(m-1, -1, -1):
                ans.append(matrix[rows][cols])
    return ans

m = 4
n = 4
matrix = [[2, 3, 4, 5], [1, 2, 3, 4], [5, 4, 4, 3], [2, 7, 3, 4]]
print(wave_print(matrix, m, n))
