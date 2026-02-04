class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        res = ""

        try:
            i = 0
            while True:
                try_letter = strs[0][i]
                eq = True
                for word in strs:
                    if word[i] != try_letter:
                        eq = False
                if eq:
                    res += try_letter
                else:
                    return res
                i += 1
        except:
            return res

solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix(["cir","car"]))



