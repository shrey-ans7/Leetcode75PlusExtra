class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        end=len(fruits)
        l=0
        r=1
        tracker={}
        res=1
        count=1
        tracker[fruits[l]]=1
        while(l<r and r<end):
            f=fruits[r]
            if f in tracker:
                tracker[f]+=1
                res=max(res,r-l+1)
            else:
                count+=1
                tracker[f]=1
                if count>2:
                    while(l<r):
                        tracker[fruits[l]]-=1
                        if tracker[fruits[l]]==0:
                            del tracker[fruits[l]]
                            l+=1
                            break
                        l+=1
                    count-=1
                res=max(res,r-l+1)
                    
            r+=1
        return res

