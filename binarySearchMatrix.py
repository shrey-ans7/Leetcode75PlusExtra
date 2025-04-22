class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix)-1
        def search(row):
            low=0
            high=len(row)-1
            while low<=high:
                mid=low+(high-low)//2
                if row[mid]==target:
                    return True
                elif row[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return False


        while low<=high:
            mid=low+(high-low)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]>target:
                high=mid-1
            else:
                if mid+1>high or matrix[mid+1][0]>target:
                    return search(matrix[mid])
                else:
                    low=mid+1
        return False

        
