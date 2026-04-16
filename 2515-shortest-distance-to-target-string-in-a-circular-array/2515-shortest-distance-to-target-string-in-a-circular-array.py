class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        mini1,mini2 = n,n

        if target not in words:
            return -1

        for i in range(n):
            if words[i] == target:
                a = abs(i-startIndex)
                if startIndex<i:
                    b =  n-i+startIndex
                else:
                    b = n-startIndex+i
                mini1 = min(a,b)
                print(i,a,b,mini1)
            mini2 = min(mini2,mini1)

        return mini2