class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        left = [(target - i) for i in position]
        
        leftmap = []
        for i in range(len(position)):
            leftmap.append((left[i],speed[i]))
        leftmap = sorted(leftmap)
        fleet = 1
        fleetTime = leftmap[0][0]/leftmap[0][1]
        for lf,sp in leftmap:
            time = lf / sp
            if time <= fleetTime:
                continue;
            else:
                fleetTime = time
                fleet+=1
        return fleet



        

