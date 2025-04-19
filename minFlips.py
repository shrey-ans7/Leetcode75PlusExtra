class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        d=(a|b)^c
        c1=c
        a1=a
        b1=b
        count=0
        last_bit_c1=0
        last_bit_a1=0
        last_bit_b1=0
        while d:
            count+=d&1
            d=d>>1
        while a1 or b1 or c1:
            last_bit_c1=c1&1
            last_bit_a1=a1&1
            last_bit_b1=b1&1
            if last_bit_c1==0:
                if last_bit_a1==last_bit_b1==1:
                    count+=1
            c1=c1>>1
            a1=a1>>1
            b1=b1>>1
        return count


