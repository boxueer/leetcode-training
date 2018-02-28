'''
Input: 123
Output:  321

Input: -123
Output: -321

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        d=str(x)
        c=len(d)
        pp=""
        f=0
        if d[0]!='-':
            f=1
        for i in range(c):
             if (d[c-i-1]!='-'):
                pp+=d[c-i-1]
             
                
        pp=int(pp)
        if (f==0):
            pp=-pp
        if (abs(pp)>=2**31):
            pp=0
        return pp
