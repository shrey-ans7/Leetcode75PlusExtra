class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n==0:
            return 0
        mod = 10**9 + 7
        evens = (n + 1) // 2  
        primes = n // 2         
        
        return (pow(5, evens, mod) * pow(4, primes, mod)) % mod
        
        
