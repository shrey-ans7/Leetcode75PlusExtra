from typing import List
import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fir=sys.maxsize
        sec=sys.maxsize
        for num in nums:
            if num<=fir:
                fir = num
            elif num<=sec:
                sec=num
            else:
                return True
        return False
