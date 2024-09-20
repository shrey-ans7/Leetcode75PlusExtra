class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = ["N","E","S","W"]
        size=len(dirs)
        pos=0
        cood=[0,0]
        dist=0
        temp=set()
        for obs in obstacles:
            temp.add(str(obs))
        obstacles=temp
        for command in commands:
            if command<0:
                if command==-1:
                    pos+=1
                    if pos==size:
                        pos=0
                else:
                    pos-=1
                    if pos<0:
                        pos=size-1
                continue
            else:
                if dirs[pos]=="N":
                    for k in range(command):
                        cood[1]+=1
                        if str(cood) in obstacles:
                            cood[1]-=1
                            break
                elif dirs[pos]=="E":
                    for k in range(command):
                        cood[0]+=1
                        if str(cood) in obstacles:
                            cood[0]-=1
                            break
                elif dirs[pos]=="S":
                    for k in range(command):
                        cood[1]-=1
                        if str(cood) in obstacles:
                            cood[1]+=1
                            break
                elif dirs[pos]=="W":
                    for k in range(command):
                        cood[0]-=1
                        if str(cood) in obstacles:
                            cood[0]+=1
                            break
                dist=max(dist,cood[0]**2+cood[1]**2)
        return dist
                    



        
