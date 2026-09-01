class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        is_negative=x<0
        x=abs(x)
        
        while x>0:
            rem=x%10
            rev=(rev*10)+rem
            x=x//10
        if is_negative:
                rev=-rev
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return rev
        

x=int(input("Enter a no: "))
sol=Solution()
s=sol.reverse(x)
print(s)