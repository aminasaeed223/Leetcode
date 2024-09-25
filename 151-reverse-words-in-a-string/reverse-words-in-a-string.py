class Solution:
    def reverseWords(self, s: str) -> str:
       words = s.split()
       reveresed_words = words[::-1]
       return " ".join(reveresed_words)
        