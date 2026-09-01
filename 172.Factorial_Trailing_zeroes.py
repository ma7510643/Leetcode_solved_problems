class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n>0: # 10
            n//=5   # n=n//5
            ans+=n  # 
        return ans

n = int(input("Enter a number: "))

sol=Solution.trailingZeroes(Solution,n)
print(sol)