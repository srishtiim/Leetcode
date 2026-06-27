class Solution(object):
    def isSubsequence(self, s, t):
        pointers, pointert = 0, 0

        while pointers < len(s) and pointert < len(t):
            if s[pointers] == t[pointert]:
                pointers += 1
            pointert += 1
        
        return pointers == len(s)

        