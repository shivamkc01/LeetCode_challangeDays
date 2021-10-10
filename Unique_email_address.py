# Question = https://leetcode.com/problems/unique-email-addresses/

#-----Time Complexity-----> O(n)
#-----Space Complexity----> O(n), where n is number of unique email present

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #---------Examples------------#
        # test.email+alex@leetcode.com
        # a = []
        # first = test.email+
        # last = leetcode.com
        # first = test.email
        # a = test.email@leetcode.com
        # return length of a 
        #-----------------------------#
        a = set()
        for email in emails:
            first, last = email.split('@')
            if '+' in first:
                first = first[:first.index('+')]
                print(first)
            a.add(first.replace('.', '') + '@' + last)
        return len(a)