
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for index in range(m, len(nums1)):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()


