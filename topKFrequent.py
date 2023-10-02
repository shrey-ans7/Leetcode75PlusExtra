import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder=[]
        tracker={}
        ans=[]
        for i in nums:
            if i not in tracker.keys():
                tracker[i]=1
            else:
                tracker[i]+=1

        for i,j in tracker.items():
            holder.append([i,j])
        holder.sort(key=lambda x:-x[1])
        for i in range(k):
            ans.append(holder[i][0])
        return ans
