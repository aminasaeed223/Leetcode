class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q=deque(range(len(deck)))
        result=[0]*len(deck)
        for value in deck:
            index=q.popleft()
            result[index]=value
            if q:
                x=q.popleft()
                q.append(x)
        return result
        