class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordered = { c: i for i , c in enumerate(order)}
        for i in range (len(words)-1):
            w1 = words [i]
            w2 = words[i +1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if ordered [w2[j]] < ordered [w1[j]]:
                        return False
                    break
        return True
        