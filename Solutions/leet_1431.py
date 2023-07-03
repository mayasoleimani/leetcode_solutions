class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        returnList=[]
        maxx=max(candies)

        for i in candies:

            if (i+extraCandies > maxx) or (i+extraCandies == maxx):
                returnList.append(True)
            else:
                returnList.append(False)


        return(returnList)
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
