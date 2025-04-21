class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        size1=len(strs[0])
        size2=len(strs[len(strs)-1])
        i=0
        while(i<size1 and i<size2):
            if strs[0][i]==strs[len(strs)-1][i]:
                i+=1
            else:
                return strs[0][0:i]
        return strs[0][0:i]
        
        
