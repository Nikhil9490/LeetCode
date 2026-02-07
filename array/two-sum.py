class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i] #checking if we have the "difference" number which makes up the target when added with ith number
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i #assigning number to its index in the hashmap

        