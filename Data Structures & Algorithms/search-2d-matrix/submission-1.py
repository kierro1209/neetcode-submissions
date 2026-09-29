class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix)-1
        if i == j:
            if target in matrix[0]:
                return True
            else:
                return False
        while i < j:
            print("i: "+str(i)+" j: "+str(j))
            if matrix[i][-1] < target:
                i += 1
            elif matrix[j][0] > target:
                j -= 1
            if matrix[i][0] == target or matrix[j][0] == target:
                return True
        
        k, x = 1, len(matrix[i])-1
        while k < x:
            print("left: "+str(matrix[i][k])+" right: "+str(matrix[i][x]))
            if matrix[i][k] < target:
                k += 1
            elif matrix[i][x] > target:
                x -=1
            if matrix[i][k] == target or matrix[i][x] == target:
                return True
        return False