from typing import List

class Solution:
 
    def removeElement(nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

def main():
    alist: List[int] = [1, 2, 3, 4]
    val: int = 3
    print("Original list:", alist)
    Solution.removeElement(alist, val)
    print("List after removing elements:", alist)

if __name__ == "__main__":
    main()
