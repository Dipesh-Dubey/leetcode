class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""

        def dfs(i,path,oc,cc):
            if oc>n or cc>n or oc<cc:
                return
            if i==2*n:
                if oc==cc:
                    res.append(path[:])
                return
            
            path+="("
            oc+=1
            print(path)
            dfs(i+1,path,oc,cc)

            path = path[:-1]
            print(path)
            oc-=1

            path += ")"
            cc+=1
            print(path)
            dfs(i+1,path,oc,cc)
        
        dfs(0,path,0,0)
        return res