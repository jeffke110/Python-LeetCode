from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            left : int = 0
            right : int = len(nums)
            while(left < right):
                middle : int = left + (right - left) // 2
                if(nums[middle] == target):
                    return middle
                elif(nums[middle] < target):
                    left+= 1
                else:
                    right -=1

            return left
