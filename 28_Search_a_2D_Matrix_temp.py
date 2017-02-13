class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        _list = []
        for i in range(len(matrix)):
            _list.extend(matrix[i])
        head = 0
        tail = len(_list)
        if head == tail:
            return False
        while head < tail-1:
            mid = (head+tail)/2
            if _list[mid] <= target:
                head = mid
            else:
                tail = mid
        if _list[head] == target:
            return True
        else:
            return False
