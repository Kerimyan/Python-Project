# grid = [[0, 1, 0, 0],
#         [1, 1, 1, 0],
#         [0, 1, 0, 0],
#         [1, 1, 0, 0]]
#
# grid = [[1]]
#
# grid = [[0,1]]


grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 1]]


def islandPerimeter(grid):
    res = 0
    len_x = len(grid[0])
    len_y = len(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count = 4
            if grid[i][j] == 1:
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    count -= 1
                if j + 1 < len_x and grid[i][j+1] == 1:
                    count -= 1
                if i + 1 < len_y and grid[i+1][j] == 1:
                    count -= 1
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    count -= 1
                res += count
    return res



print(islandPerimeter(grid))