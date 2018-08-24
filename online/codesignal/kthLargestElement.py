import heapq


def kthLargestElement(nums, k):
    h = []
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
    popped = heapq.heappop(h)
    return popped
