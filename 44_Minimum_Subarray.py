class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if not nums:
            return None
        else:
            min_elem = min(nums)
            while nums[0] >= 0:
                del nums[0]
                if len(nums) == 0:
                    return min_elem
            else:
                min_now = nums[0]
                accum = nums[0]
                for i in range(1,len(nums)):
                    if accum+nums[i] < min_now:
                        accum += nums[i]
                        min_now = accum
                    elif accum+nums[i] < 0:
                        accum += nums[i]
                    else:
                        accum = 0
        return min_now   