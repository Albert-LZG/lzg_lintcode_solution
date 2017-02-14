class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        _min = min(nums)
        while _min != nums[0]:
            nums.append(nums[0])
            del nums[0]
        return nums