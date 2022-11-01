#13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        for i in range(len(s)):
            if s[i]=='I' and  i!=len(s)-1 and (s[i+1]=='V' or s[i+1]=='X'):              
                sum =sum-dict[s[i]]
            elif s[i]=='X' and  i!=len(s)-1 and (s[i+1]=='L' or s[i+1]=='C'):
                sum =sum-dict[s[i]]
            elif s[i]=='C' and  i!=len(s)-1 and (s[i+1]=='D' or s[i+1]=='M'):
                sum =sum-dict[s[i]]
            else:
                sum=sum+dict[s[i]]         
        return sum