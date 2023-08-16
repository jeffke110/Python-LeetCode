from typing import Set, List



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numSet = set()
        index = 0
        while index < len(nums):
            if nums[index] in numSet:
                del nums[index]
            else:
                numSet.add(nums[index])
                index += 1
        return len(nums)


        