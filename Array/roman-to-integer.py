class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict : dict[str, int] = {}
        romanDict["I"] = 1; romanDict["V"] = 5
        romanDict["X"] = 10; romanDict["L"] = 50
        romanDict["C"] = 100; romanDict["D"] = 500
        romanDict["M"] = 1000

        sum : int = 0
        index : int = 0
        for char in s:
            if index + 1 < len(s) and romanDict[char] < romanDict[s[index + 1]]:
                sum -= romanDict[char]
            else:
                sum += romanDict[char]
            index += 1
        
        return sum
    