class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.extend(nums)
        return nums

solution = Solution()

print(solution.getConcatenation([1,2,1]))
print(solution.getConcatenation([1,3,2,1]))
