# Find Median from Data Stream 295
import heapq
# Implementing a Data Structure using a class that can input data into it.
# It also has the functionality to output median of data stream at any given instance.
class MedianFinder:
    def __init__(self):
        # Initialise two Heaps, the leftHeap is a maxHeap & rightHeap a minHeap
        self.leftHeap, self.rightHeap = [], []

    def addNum(self, num) -> None:
        # We always initially add new num to leftHeap. We multiply it by -1 to convert the minHeap into MaxHeap. Python heapq module only implements minHeap.
        heapq.heappush(self.leftHeap, num * -1)

        # Checking if all elements of leftHeap are smaller than those of rightHeap
        # The condition becomes true when lefHeap has value greater tha smallest value in rightHeap which is wrong & thus we shift the value to rightHeap
        if (self.leftHeap and self.rightHeap and (-1 * self.leftHeap[0]) > self.rightHeap[0]):
            value = -1 * heapq.heappop(self.leftHeap[0])
            heapq.heappush(self.rightHeap, value)
        
        # Finally, we check if leftHeap and rightHeap are equally balanced in size
        # Check if leftHeap is greater by 2 or more elements than rightHeap
        if len(self.leftHeap) > len(self.rightHeap) + 1:
            value = -1 * heapq.heappop(self.leftHeap[0])
            heapq.heappush(self.rightHeap, value)
        # Vice Versa
        if len(self.rightHeap) > len(self.leftHeap) + 1:
            value = heapq.heappop(self.rightHeap[0])
            heapq.heappush(self.leftHeap, value * -1)

    def medianFind(self) -> float:
        if len(self.leftHeap) < len(self.rightHeap):
            return self.rightHeap[0]
        if len(self.leftHeap) > len(self.rightHeap):
            return self.leftHeap[0]
        
        return (self.leftHeap[0] + self.rightHeap[0]) / 2