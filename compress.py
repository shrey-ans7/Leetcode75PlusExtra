class Solution:
    def compress(self, chars: List[str]) -> int:
        res=[]
        count=0
        for char in chars:
            if len(res)==0:
                res.append(char)
                count=1
            elif char==res[-1]:
                count+=1
            else:
                if count>1:
                    for digit in str(count):
                        res.append(digit)
                count=1
                res.append(char)
        if count>1:
            for char in str(count):
                res.append(char)
        for i, char in enumerate(res):
            chars[i]=res[i]
        return len(res)
    


        
        
