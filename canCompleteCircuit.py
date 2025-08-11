#Soln 1:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        index=-1
        balance=0
        i=0
        size=len(gas)
        for fuel, price in zip(gas,cost):
            diff=fuel-price
            total+=diff
            balance+=diff
            if total<0:
                index=i+1
                total=0
            i+=1
        index=max(index,0)
        return index if balance>=0 else -1
#Soln 2:
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
            
            
            
            
        
