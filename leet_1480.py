class Solution(object):
    def runningSum(self, nums):
        runSum=list()
        for x in range(0,len(nums)):
            if x==0:                        #first index
                runSum.append(nums[x])
            elif x==len(nums)-1:            #last index
                runSum.append(sum(nums))
            else:                           #other indeces
                runSum.append(sum(nums[:x+1]))
        return runSum

        """
        :type nums: List[int]
        :rtype: List[int]
        """
