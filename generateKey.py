class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res=[]
        while num1 or num2 or num3:
            digit1=0
            digit2=0
            digit3=0
            if num1:
                digit1=num1%10
                num1=num1//10
            if num2:
                digit2=num2%10
                num2=num2//10
            if num3:
                digit3=num3%10
                num3=num3//10
            res.append(min(digit1,digit2,digit3))
        ans=0
        pot=1
        for digit in res:
            ans+=pot*digit
            pot*=10
        return ans
                

        
