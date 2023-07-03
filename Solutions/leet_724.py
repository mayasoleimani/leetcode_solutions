class Solution(object):
    def pivotIndex(self, nums):

        total= sum(nums)
        right_in=0
        left_in=0
        
        for i in range(len(nums)):

            right_in=total - nums[i] - left_in

            if right_in == left_in:
                print(i)
                return i
            else:
                left_in=left_in+nums[i]
        return -1

        """
        :type nums: List[int]
        :rtype: int
        """
