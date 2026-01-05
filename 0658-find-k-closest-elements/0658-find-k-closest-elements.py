class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        win = []
        for r in range(len(arr)):
            win.append(arr[r])
            if len(win) > k:
                if abs(win[-1]-x) >= abs(win[0]-x):
                    win.pop()
                else:
                    win.pop(0)
        
        return win

