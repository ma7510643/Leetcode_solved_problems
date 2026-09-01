class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, i in enumerate(nums):
            req = target - i

            if req in dict:
                return [dict[req], index]
            dict[i] = index

        


nums = int(input("nums: ")) 
target = int(input("target: "))
list=Solution.twoSum(Solution,nums,target)
print(list)
