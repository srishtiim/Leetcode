class Solution(object):
    def reverseWords(self, s):
        words = s.split()      # Removes extra spaces automatically
        words.reverse()        # Reverse the list
        return " ".join(words) # Join with a single space