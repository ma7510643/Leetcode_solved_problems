class Solution:#[9,9]
    def plusOne(digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
                if digits[i] < 9:
                        digits[i]+=1
                        return digits
                if digits[i]==9:
                        digits[-i] = 0
        return [1]+digits

    

digits = [9,9]
d = Solution.plusOne(digits)
print(d)