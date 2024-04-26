'''
Problem set is create an algorithm that returns a matching pair that sums up
to the total (target)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''Algorithm used to find the indices of two numbers that add up to the target. If there is only one solution in the array'''
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return None