class Solution:
    def countBits(self, n: int) -> List[int]:
        stack=[0]
        for i in range(1,n+1):
            count=0
            n=i
            while(n>0):
                count+=n&1
                n=n>>1
            stack.append(count)
        return stack

        
