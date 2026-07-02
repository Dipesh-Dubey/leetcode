class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        # Take first k cards
        tot = sum(cardPoints[:k])
        maxie = tot

        # swap one left card with one right card 
        for i in range(1, k + 1):
            tot = tot - cardPoints[k - i] + cardPoints[n - i]
            maxie = max(maxie, tot)

        return maxie

