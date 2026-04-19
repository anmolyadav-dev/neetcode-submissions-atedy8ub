class MedianFinder:

    def __init__(self):
        self.small, self.large = [],[]
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        #by default adding in self.small and check if size of both are approx same
        heapq.heappush(self.small,-num)
        if self.small and self.large and -self.small[0] > self.large[0]:
            x1 = -heapq.heappop(self.small)
            heapq.heappush(self.large,x1)
            
        if len(self.small) > len(self.large)+1:
            x1 = -heapq.heappop(self.small)
            heapq.heappush(self.large,x1)
        if len(self.large) > len(self.small) + 1:
            x1 = heapq.heappop(self.large)
            heapq.heappush(self.small,-x1)

        return

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (-1*self.small[0] + self.large[0])/2
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]