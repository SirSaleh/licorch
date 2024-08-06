"""k'th largest element

 Notation: we mention {X_1, X_2, ..., X_n} as the original array
            and the {X_(1), X(2),... X_(n)} as the elements
            of the sorted array. 
 using min-heap
   IDEA: literally, we want the minimum of k largest 
            elements in the heap of k largest elements,
            so using a heap, adding elements in each step
            and removing first_elements in the heap when 
            heap become k+1, which delete all elements
            lower than 
 * traverse over the input element
 * in each state add member into the min-heap 
 * as heap property meet, first element 
"""

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []

        for member in nums:
            heapq.heappush(min_heap, member)

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # the root element of heap will be the minimax
        # (smallest among k largest element)
        # of the array which as we need.
        return min_heap[0]


if __name__=="__main__":
    solver = Solution()

    assert solver.findKthLargest([3,2,1,5,6,4], 2)==5
    assert solver.findKthLargest([3,2,3,1,2,4,5,5,6], 4)==4

