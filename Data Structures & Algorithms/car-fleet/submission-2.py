class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time=distance/speed
        n=len(position)
        times=[1]*n
        for i in range(n):
            times[i]= (target-position[i])/speed[i]

        result= sorted(zip(position,times), reverse=True)
        fleet=1
        group=result[0][1]

        for pos,time in result: 
            if time>group: 
                fleet+=1
                group=time 
        
        return fleet

            