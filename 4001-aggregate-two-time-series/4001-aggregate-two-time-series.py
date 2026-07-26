class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        m,n = len(series1),len(series2)
        ans = []
        t1,t2 = 0,0

        while t1<m and t2<n:
            if series1[t1][0] == series2[t2][0]:
                ans.append([series1[t1][0], series1[t1][1]+series2[t2][1] ])
                t1+=1
                t2 += 1
        
            elif series1[t1][0] < series2[t2][0]:
                ans.append([series1[t1][0], series1[t1][1]+series2[t2][1] ])
                t1+=1
        
            else:
                ans.append([series2[t2][0], series1[t1][1]+series2[t2][1] ])
                t2 +=1

        while t1<m:
            ans.append(series1[t1])
            t1+=1
        while t2<n:
            ans.append(series2[t2])
            t2+=1
        return ans
            
            