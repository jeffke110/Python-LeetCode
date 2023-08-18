from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        isPlusOne : bool = False
        if digits:
            if digits[0] == 9:
                digits[0] = 0
                isPlusOne = True
            else:
                digits[0] += 1

            for index in range(1, len(digits)):
                if digits[index] == 9 and isPlusOne:
                    digits[index] = 0
                    isPlusOne = True
                elif digits[index] != 9 and isPlusOne:
                    digits[index] += 1
                    isPlusOne = False
            digits.reverse()
            if isPlusOne:
                digits.insert(0, 1)

        return digits