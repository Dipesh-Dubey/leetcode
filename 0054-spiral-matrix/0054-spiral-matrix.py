class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row,c = len(matrix) , len(matrix[0])
        t , b ,l , r = 0, row-1, 0, c-1

        while len(res)<row*c:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t += 1
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r -=1

            if t <= b:
                for i in range(r,l-1,-1):
                    res.append(matrix[b][i])
                b -=1
            if l<=r:
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l +=1
        return res



        
