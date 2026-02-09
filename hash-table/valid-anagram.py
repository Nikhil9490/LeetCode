class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        str1 = s.lower()
        str2 = t.lower()

        str1 = str1.replace(" ", "")
        str2 = str2.replace(" ", "")


        counts = [0] * 26

        for char in str1:
            counts[ord(char)-ord('a')]+= 1
        for char in str2:
            counts[ord(char)-ord('a')]-= 1

        for count in counts:
            if count!=0:
                return False
        return True
        

