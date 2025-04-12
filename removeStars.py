class Solution:
    res=None
    def removeStars(self, s: str) -> str:
        res=[]
        for char in s:
            if char=="*":
                if not res:
                    continue
                res.pop()
            else:
                res.append(char)
        return "".join(res)
        
