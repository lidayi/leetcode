class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        begin = 0
        end = len(s)-1
        strlist = [i for i in s]
        while(begin < end):
            camp =  strlist[begin]
            strlist[begin] = strlist[end]
            strlist[end] = camp
            begin +=1
            end -=1
        return ''.join(strlist)
        
