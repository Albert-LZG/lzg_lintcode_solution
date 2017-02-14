class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return None
        else:
            max_elem = max(nums)
            while nums[0] <= 0:
                del nums[0]
                if len(nums) == 0:
                    return max_elem
            else:
                max_now = nums[0]
                accum = nums[0]
                for i in range(1,len(nums)):
                    if accum+nums[i] > max_now:
                        accum += nums[i]
                        max_now = accum
                    elif accum+nums[i] > 0:
                        accum += nums[i]
                    else:
                        accum = 0
        return max_now    