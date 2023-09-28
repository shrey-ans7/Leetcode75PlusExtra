class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        temp = 1
        count=0
        for i in nums:
            if i == 0:
                # index_set.add(index)
                count+=1
                continue
            temp *=i
        for i in nums:
            if i==0:
                if(count>1):
                    answer.append(0)
                else:
                    answer.append(temp)
            elif count>0:
                answer.append(0)
            else:
                answer.append(int(temp/i))
        return answer
