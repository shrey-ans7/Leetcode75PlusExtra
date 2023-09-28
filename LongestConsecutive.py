class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        og_set = set(nums)
        longest = len(og_set)
        done = set()
        length=0
        for i in og_set:
            if i in done:
                continue
            else:
                length1 = 1
                while i+length1 in og_set:
                    done.add(i+length1)
                    length1+=1
                length2 = 1
                while i-length2 in og_set:
                    done.add(i-length2)
                    length2+=1
                length=max(length,length1+length2-1)
        return length
