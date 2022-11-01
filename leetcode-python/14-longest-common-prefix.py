class Solution(object):
    def longestCommonPrefix(self, strs):
        output=''
        for i in range(len(min(strs))):
            letter=strs[0][i]
            print(letter)
            for item in strs:
                if item[i]!=letter:
                    print("item:",item[i])
                    return output
            output=output+letter
        return output