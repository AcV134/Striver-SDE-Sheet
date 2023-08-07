class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = 0
        count = 0
        n = len(nums)//2
        for i in nums:
            if count == 0:
                element = i
            count += 1 if element == i else (-1)
        return element
