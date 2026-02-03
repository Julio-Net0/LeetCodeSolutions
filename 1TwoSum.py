class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        values_map = dict()

        for i, num in enumerate(nums):

            value_to_target = target - num

            if(value_to_target in values_map):
                return [values_map[value_to_target], i]
            else:
                values_map[num] = i
            

solution = Solution()

print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3,3], 6))
