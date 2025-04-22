class Segment:
    def __init__(self, l:int, r:int):
        self.l=l
        self.r=r
        self.left=None
        self.right=None
        self.sum=-sys.maxsize
class NumArray:

    def __init__(self, nums: List[int]):
        def build(l,r):
            if l==r:
                segment=Segment(l,r)
                segment.sum=nums[l]
                return segment
            mid=l+(r-l)//2
            segment=Segment(l,r)
            left=build(l,mid)
            right=build(mid+1,r)
            segment.sum=left.sum+right.sum
            segment.left=left
            segment.right=right
            return segment
        self.root=build(0,len(nums)-1)
        
    def update(self, index: int, val: int) -> None:
        def update_node(root,index,val):
            if root.l==root.r==index:
                root.sum=val
                return root
            mid=root.l+(root.r-root.l)//2
            if index<=mid:
                root.left=update_node(root.left,index,val)
            else:
                root.right=update_node(root.right,index,val)
            root.sum=root.left.sum+root.right.sum
            return root
        self.root=update_node(self.root,index,val)

    
        

    def sumRange(self, left: int, right: int) -> int:
        def calc_sum(root,l,r):
            if root.l == l and root.r == r:
                return root.sum
            mid=root.l+(root.r-root.l)//2
            if l>mid:
                return calc_sum(root.right,l,r)
            elif r<=mid:
                return calc_sum(root.left,l,r)
            else:
                return calc_sum(root.left,l,mid)+calc_sum(root.right,mid+1,r)
        return calc_sum(self.root,left,right)

        
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
