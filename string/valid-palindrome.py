class Solution:
    def isPalindrome(self, s: str) -> bool:
        c= ""
        for i in s:
            if i.isalnum(): #check every character if its alphanumeric. if it is, then append it to c string.
                c=c+i.lower()
        return c == c[::-1] #check if both sides are equal
        