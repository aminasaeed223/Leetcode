class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse = []
        for word in words:
            reverse_word = word[::-1]
            reverse.append(reverse_word)
        return " ".join(reverse)
        