class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = dict()
        for i in range(len(nums)):
            value = target - nums[i]
            # print(value,i,nums[i])
            if value in new_nums:
                return [new_nums[value],i]
            if nums[i] not in new_nums:
                new_nums[nums[i]] = i
