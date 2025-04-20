from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        pairs = [0 for _ in range(n)]
        potions.sort()                       
        for i, spell in enumerate(spells):
            low, high = 0, m - 1
            # find the first j with potions[j]*spell >= success
            while low < high:
                mid = (low + high) // 2
                if potions[mid] * spell < success:
                    low = mid + 1
                else:
                    high = mid
            # after the loop low==high; check if it actually works
            idx = low if potions[low] * spell >= success else m
            pairs[i] = m - idx             # ← use idx, not i

        return pairs
