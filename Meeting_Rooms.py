# Question : https://leetcode.com/problems/meeting-rooms/

#----Time Complexity----------> O(n. logn)
#----Space Complecity---------> O(1), constant

class Solution:
    def canAttendMeetings(intervals):

        # [[7, 10], [2, 4]]
        # 0----5----10----15----20----25----30
        #   |-|  |--|
        #   2 4  7  10
        # return TRUE

        intervals.sort()     # O(n .logn)
        last_end = -1
        for start, end in intervals:    # O(n)
            if last_end <= start:
                last_end = end
            else:
                return False
        return True
