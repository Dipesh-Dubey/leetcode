class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        combo = s + s
        if goal in combo:
            return True
        return False
