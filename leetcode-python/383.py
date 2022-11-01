class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in magazine:
            if i in ransomNote:
                ransomNote=ransomNote.replace(i,"",1)
                magazine=magazine.replace(i,"",1)
        print(magazine)
        if len(ransomNote)==0:
            return True
        else:
            return False