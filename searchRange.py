class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size=len(nums)
        def find_first(l,r):
            idx=-1
            while(l<=r):
                mid=l+(r-l)//2
                if nums[mid]==target:
                    idx=mid
                    r=mid-1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return idx
        def find_last(l,r):
            idx=-1
            while(l<=r):
                mid=l+(r-l+1)//2
                if nums[mid]==target:
                    idx=mid
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return idx

        f=find_first(0,size-1)
        l=find_last(0,size-1)
        return [f,l]
        
        
