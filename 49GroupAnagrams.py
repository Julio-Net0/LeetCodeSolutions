class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = {}

        for word in strs:
            freqArray = [0] * 26
            for char in word:
                freqArray[ord(char) - ord('a')] += 1

            key = tuple(freqArray)

            if key not in res:
               res[key] = []
            res[key].append(word)

        return list(res.values())

solution = Solution()

print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))
