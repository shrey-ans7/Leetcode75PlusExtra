class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        bansR=0
        bansD=0
        votesR=0
        votesD=0
        totBansR=0
        totBansD=0
        for senator in senate:
            if senator=="D":
                votesD+=1
            else:
                votesR+=1
        senate=list(senate)
        while(votesR-totBansR>0 and votesD-totBansD>0):
            for i,senator in enumerate(senate):
                if senator=="D":
                    if bansD>0:
                        bansD-=1
                        senate[i]="S"
                    else:
                        bansR+=1
                        totBansR+=1
                elif senator=="R":
                    if bansR>0:
                        bansR-=1
                        senate[i]="S"
                    else:
                        bansD+=1
                        totBansD+=1
        if votesR-totBansR<=0:
            return "Dire"
        return "Radiant"
        
