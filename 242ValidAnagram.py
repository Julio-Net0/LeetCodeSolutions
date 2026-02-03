from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        counter_s = Counter(s)
        counter_t = Counter(t)

        return True if counter_s == counter_t else False
        

        
solution = Solution()

print(solution.isAnagram("anagram","nagaram"))
print(solution.isAnagram("rat","car"))
print(solution.isAnagram("aa","a"))
print(solution.isAnagram("aacc","ccac"))

