import copy
matrix=[[1,2,3],[4,5,6],[7,8,9]]

# res = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def rotate(matrix: list[list[int]]):
    from copy import deepcopy
    res = copy.deepcopy(matrix)
    ind = 0
    for m in res[::-1]:
        for i in range(len(m)):
            matrix[i][ind] = m[i]
        ind += 1





print(rotate(matrix))