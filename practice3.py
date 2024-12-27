class Solution:
    def checkStatus(self, a, b, flag):
        if a < 0 and b < 0 and flag == True:
            return True
        elif a < 0 and b < 0 and flag == False:
            return False
        else:
            return False

solution = Solution()

print(solution.checkStatus(1,-1,False))
print(solution.checkStatus(-1,-1,True))
print(solution.checkStatus(1,1,True))
print(solution.checkStatus(-4,-5,False))