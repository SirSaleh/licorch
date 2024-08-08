"""Given an integer array nums and an integer k, 
    return the k most frequent elements. You may return the answer in any order.
"""

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        heap = []
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))
        
        results = []
        while len(results) < k:
            results.append(heapq.heappop(heap)[1])
        
        return results


if __name__=="__main__":
    solution = Solution()

    assert solution.topKFrequent([1,1,1,2,2,3], 2)==[1, 2]
    assert solution.topKFrequent([1], 1)==[1]
