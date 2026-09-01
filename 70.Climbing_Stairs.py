class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev1 = 2
        current = 0
        if n == 1:
            return n
        if n == 2:
            return n
        else:
            for i in range(3,n+1):
                current=prev1+prev2
                prev2=prev1
                prev1=current
            return current

n = int(input("Enter the no. of stairs: "))
a = Solution.climbStairs(Solution,n)
print(a)

