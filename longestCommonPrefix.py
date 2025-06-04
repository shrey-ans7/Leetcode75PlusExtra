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
        
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        curr_range=len(strs[0])
        chars={}
        count=0
        for char in strs[0]:
            chars[count]=char
            count+=1
        for i in range(1,len(strs)):
            curr_range=min(curr_range,len(strs[i]))
            for j in range(len(strs[i])):
                if j not in chars:
                    curr_range=min(curr_range,j)
                    break
                if j==curr_range:
                    break
                if chars[j]==strs[i][j]:
                    continue
                else:
                    curr_range=min(curr_range,j)
                    break
        return strs[0][:curr_range]


                
        
        
