class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size1=len(haystack)
        size2=len(needle)
        if size2==0:
            return 0
        if size2>size1:
            return -1
        found=False
        for i in range(size1-size2+1):
            found=True
            for j in range(size2):
                if haystack[i+j]==needle[j]:
                    continue
                else:
                    found=False
                    break
            if found:
                return i
        return -1
            
