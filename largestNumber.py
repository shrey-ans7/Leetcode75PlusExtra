from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # convert to strings
        A = list(map(str, nums))

        # sort with inline lambda comparator:
        A.sort(key=cmp_to_key(
            lambda a, b: -1 if a + b > b + a
                        else 1
        ))

        # handle the all-zero case
        return "0" if A and A[0] == "0" else "".join(A)
