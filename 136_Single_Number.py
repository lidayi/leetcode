class Solution(object):
    def singleNumber(self, A):
        num = 0
        for ele in A:
            num = num^ele
        return num
