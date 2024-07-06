class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        last = len(gas)-1
        diffTot = 0
        i=0
        index=0
        while index<=last:
            diff = gas[i] - cost[i]
            diffTot += diff
            if diffTot<0:
                diffTot=0
                index+=1
                i=index
                continue
            i+=1
            if i>last:
                i=0
            if i==index:
                return index
        return -1
            
            
            
            
        
