class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged=''
        i=0
        j=0
        

        while len(word1)>i and len(word2)>j:
            
            merged=merged+word1[i]
            merged=merged+word2[j]
            i+=1
            j+=1

            if i>=len(word1):
                merged=merged+word2[j:]
            elif j>=len(word2):
                merged=merged+word1[i:]

        return merged
