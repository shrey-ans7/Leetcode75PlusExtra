class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        size = len(hand)
        if size%groupSize!=0:
            return False
        numBuckets = size//groupSize
        sets = [[] for _ in range(numBuckets)]
        hand.sort()
        for card in hand:
            flag = False
            for bucket in sets:
                if bucket:
                    if bucket[-1]==card-1 and len(bucket)<groupSize:
                        bucket.append(card)
                        flag = True
                        break
                else:
                    bucket.append(card)
                    flag = True
                    break
            if not flag:
                return flag
        return flag
                
                        
            
        
