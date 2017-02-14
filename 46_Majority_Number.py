class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        if not nums:
            return None
        else:
            nums.sort()
            elem_max = nums[0]
            elem_now = nums[0]
            count_max = 0
            count = 0
            nums_len = len(nums)
            for i in range(0, nums_len):
                if nums[i] == elem_now:
                    count += 1
                    if elem_now == elem_max:
                        count_max += 1
                    elif count > count_max:
                        count_max = count
                        elem_max = elem_now
                else:
                    count = 1
                    elem_now = nums[i]
        if count_max > nums_len/2:
            return elem_max
        else:
            return None