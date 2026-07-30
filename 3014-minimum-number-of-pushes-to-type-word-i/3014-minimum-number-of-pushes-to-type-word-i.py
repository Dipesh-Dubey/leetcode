class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        counter = res =  0
        level = 1
        for i in range(n):
            if counter >= 8:
                counter = 0
                level += 1

            counter += 1
            res += level
        return res

