# Solution:
def canAttendMeetings(intervals):
    intervals.sort()
    last_end = -1
    for start, end in intervals:
        if last_end <= start:
            last_end = end
        else:
            return False
    return True

a = [[7, 10], [2, 4]]
res = canAttendMeetings(a)
print(res)