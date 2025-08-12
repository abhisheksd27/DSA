class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i, n in enumerate(nums):
            d= target - n
            if d in h:
                return [h[d],i]
            else:
                h[n]=i
        return 
        