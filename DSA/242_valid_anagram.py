#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for letter in s:
            if letter in s_dict.keys():
                s_dict[letter] = s_dict[letter] + 1
            else:
                s_dict[letter] = 1

        t_dict = {}
        for letter in t:
            if letter in t_dict.keys():
                t_dict[letter] = t_dict[letter] + 1
            else:
                t_dict[letter] = 1
        return s_dict == t_dict