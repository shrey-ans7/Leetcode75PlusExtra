class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearchL1(matrix, target):
            def search(nums, target):
                low=0
                high=len(nums)
                mid = (low+high)//2
                print(nums, low, high, mid)
                if low==high:
                    return -1
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    return search(nums[0:mid], target)
                else:
                    tmp=search(nums[mid+1:high], target)
                    print(tmp)
                    if(tmp==-1):
                        return -1
                    return mid+1+tmp
            low=0
            high=len(matrix)
            mid=low+high//2
            if low==high-1:
                return search(matrix[low],target)
            elif matrix[mid][0]==target:
                return 0
            elif matrix[mid][0]>target:
                return binarySearchL1(matrix[0:mid],target)
            else:
                if mid+1==high or matrix[mid+1][0]>target:
                    return search(matrix[mid], target)
                tmp=binarySearchL1(matrix[mid+1:high], target)
                if(tmp==-1):
                    return -1
                return mid+1+tmp
        ans=binarySearchL1(matrix, target)
        if ans==-1:
            return False
        return True
