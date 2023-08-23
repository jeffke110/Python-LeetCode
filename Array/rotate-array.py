from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        rotateArray = nums[len(nums) - k: len(nums)]
        for index in range(len(nums) - k, len(nums)):
            nums.pop()
        rotateArray.reverse()
        for index in range(len(rotateArray)):
            nums.insert(0, rotateArray[index])
