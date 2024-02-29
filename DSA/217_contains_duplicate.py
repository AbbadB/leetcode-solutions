#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        if len(nums) > len(no_duplicates):
            return True
        else:
            False