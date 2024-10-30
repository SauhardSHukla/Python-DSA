def checkXMatrix(grid):
    # write your code here !!!
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:  # main diagonal or anti-diagonal element
                if grid[i][j] == 0:
                    return False
            else:  # off-diagonal elements
                if grid[i][j] != 0:
                    return False
    
    return True

def main():
    grid_str = input()
    grid = eval(grid_str)

    if checkXMatrix(grid):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
