class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//','/')
        stack = []

        path = path.split('/')
        for dir in path:
            if dir == "" or dir == ".":
                continue
            if dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        
        return "/" + "/".join(stack)
            

            