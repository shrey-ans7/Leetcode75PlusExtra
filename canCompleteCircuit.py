class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        last = len(gas)-1
        visited = set()
        diffTot = 0
        i=0
        visited=set()
        index=0
        while index<=last:
            diff = gas[i] - cost[i]
            diffTot += diff
            visited.add(i)
            if diffTot<0:
                diffTot=0
                index+=1
                i=index
                visited = set()
                continue
            i+=1
            if i>last:
                i=0
            if i in visited:
                return index
        return -1
            
            
            
            
        
