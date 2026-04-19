class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heapq.heapify(dist)
        for i in range(len(points)):
            heapq.heappush(dist,(-(points[i][0]**2 + points[i][1]**2),i))
            if len(dist) > k:
                heapq.heappop(dist)
        ans = []
        print(dist,points)
        for vals in dist:
            ans.append(points[vals[1]])
        return ans