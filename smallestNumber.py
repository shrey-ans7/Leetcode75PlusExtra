class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        digits=[]
        zero_count=0
        is_negative=False
        pot=1
        if num<0:
            is_negative=True
            num*=-1
        while num:
            digit=num%10
            num=num//10
            pot*=10
            if digit==0:
                zero_count+=1
                continue
            digits.append(digit)
        pot//=10
        if is_negative:
            digits.sort(key=lambda num:-num)
        else:
            digits.sort()
        res=0
        res+=(pot)*digits[0]
        pot//=10
        if not is_negative:
            for i in range(zero_count):
                pot//=10

            for i in range(1,len(digits)):
                res+=digits[i]*pot
                pot//=10
        else:
            for i in range(1,len(digits)):
                res+=digits[i]*pot
                pot//=10
        return res if not is_negative else -res
        






        
