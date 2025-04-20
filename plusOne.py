class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size=len(digits)
        prev=digits[size-1]+1
        digits[size-1]=prev%10
        prev=prev//10
        for i in range(size-2,-1,-1):
            digit=digits[i]+prev
            digits[i]=digit%10
            prev=digit//10
        if prev>0:
            digits.insert(0,prev)
        return digits
        
