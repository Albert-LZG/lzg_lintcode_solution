# nest = [[1,1],2,[1,1,[3,4,[5,6]]]]
# res = []

# def flatten(nest):
#     # Write your code here
#     if nest:
#         _flatten(nest)
#         print res
#     else:
#         print res.append([])

# def _flatten(temp_list):
#     i = 0
#     while i < len(temp_list):
#         if isinstance(temp_list[i],int):
#             res.append(temp_list[i])
#         else:
#             _flatten(temp_list[i])
#         i += 1
#     return res

# flatten(nest)

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    res = []
    def flatten(self, nestedList):
        # Write your code here
        if nestedList:
            self._flatten(nestedList)
            return Solution.res
        else:
            return Solution.res.append([])
    
    
    def _flatten(self, temp_list):
        if isinstance(temp_list, int):
            Solution.res.append(temp_list)
            return Solution.res
        else:
            i = 0
            while i < len(temp_list):
                if isinstance(temp_list[i], int):
                    Solution.res.append(temp_list[i])
                else:
                    self._flatten(temp_list[i])
                i += 1
            return Solution.res