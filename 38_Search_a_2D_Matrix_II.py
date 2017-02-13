class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        count = 0
        for i in range(len(matrix)):
            temp = matrix[i]
            count += temp.count(target)
        return count