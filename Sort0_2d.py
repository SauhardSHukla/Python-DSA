from typing import List

def set_rows(mat,rows):
    for i in range(len(mat)):
        if mat[rows][i]!=0:
            mat[rows][i]=-1

def set_cols(mat,cols):
    for j in range(len(mat[0])):
        if mat[j][cols] !=0:
            mat[j][cols]=-1

def set0(matrix: List[List[int]]) -> None:
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                set_rows(matrix,i)
                set_cols(matrix,j)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] ==-1:
                matrix[i][j]=0
        
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

set0(matrix)
print(matrix)
