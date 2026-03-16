class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=0
        for i in range(k,k+3):
            if needle == haystack[k:k+3]:
                return k
            k=k+1
        return -1
        