class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = dict()
        result = list()
        n = len(nums)//3
        for i in nums:
            if i not in counter.keys():
                counter[i] = 0
            counter[i]+=1
        print(counter)
        for i in counter:
            if counter[i]>n:
                result.append(i)
        return result
