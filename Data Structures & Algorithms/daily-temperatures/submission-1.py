class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        i=0
        while i < len(temperatures):
            if not stack:
                stack.append(i)
                i+=1
            else:
                app = stack[-1]
                while stack and temperatures[i]>temperatures[app]:
                    res[app] = i-app
                    stack.pop()
                    if stack:
                        app=stack[-1]
                stack.append(i)
                i+=1
        return res