class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        index = -1
        for i in range(len(word)):
            stack.append(word[i])
            if word[i] == ch:
                index = i
                break
        if index == -1:
            return word
        st = ""
        while stack:
            st = st + stack.pop()
        return st + word[index +1 :]