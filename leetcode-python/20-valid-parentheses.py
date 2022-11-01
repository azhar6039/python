class Solution(object):
    def isValid(self, s):
        for i in range(len(s)):
            if s[i] =='(' and s[i+1]!=')':
                return False
            if s[i] =='{' and s[i+1]!='}':
                return False
            if s[i] =='[' and s[i+1]!=']':
                return False
        return True