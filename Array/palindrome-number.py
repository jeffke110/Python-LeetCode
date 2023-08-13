


class Solution:
    def isPalindromeOne(self, x: int) -> bool:
        tempString = str(x)
        reverseString = tempString[::-1]
        return tempString == reverseString

    def isPalindromeTwo(self, x: int) -> bool:
        inputString  = str(x)
        reverseString = ''.join(reversed(inputString))
        return reverseString == inputString

    
    def isPalindromeThree(self, x: int) -> bool:
        inputString = str(x)
        reversedString = ""
        for char in inputString:
            reversedString = char + reversedString
        return reversedString == inputString
    
    def isPalindromeFour(self, x : int) -> bool:
        inputString = str(x)
        reversedString = "".join(char for char in reversed(inputString))
        return inputString == reversedString



