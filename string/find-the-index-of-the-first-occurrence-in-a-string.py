class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=0
        for i in range(k,k+len(needle)):
            if needle == haystack[k:k+len(needle)]:
                return k
            k=k+1
        return -1
        