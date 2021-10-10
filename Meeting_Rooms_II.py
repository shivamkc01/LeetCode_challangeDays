# Question in interviewbit : https://www.interviewbit.com/problems/meeting-rooms/#
# Question in LeetCode : https://leetcode.com/problems/meeting-rooms-ii/


#### Time Complexity    --> O(n. logn)
#### Space Complexity   --> O(n)

import heapq
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        """
        0--5--10--15--20--25--30
        |----------|
        |----------------------|
           |---|   |---|


        [[0, 15], [0, 30], [5, 10], [15, 20], [21, 25]] -> Sort()
        """
        # heap = [15], [15, 30], [10, 15, 30], [15, 20, 30], [21, 20, 30]
        # meeting_rooms = 1, 2, 3 -> 3 is our answer
        A.sort()    # --> O(n. logn)
        meeting_rooms = 1
        heap = [A[0][1]]
        for start, end in A[1:]:
            if heap[0] <= start:            # O(n.logk), k is no of item in heap
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            meeting_rooms = max(meeting_rooms, len(heap))
        return meeting_rooms


