nums=[2,7,11,5,3]
target=9
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for x in range(len(nums)):
        if target-nums[x] in nums and x!= nums.index(target-nums[x]):
            return [x,nums.index(target-nums[x])]
twoSum()