class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            print("Strings are not same size")
            return False
        
        s = s.lower()
        t = t.lower()
        sMap = {}
        tMap = {}
        
        for char in s:
            if char in sMap:
                sMap[char] += 1
            else:
                sMap[char] = 1
        
        for char in t:
            if char in tMap:
                tMap[char] += 1
            else:
                tMap[char] = 1
        
        for char, count in sMap.items():
            if char not in tMap or tMap[char] != count:
                return False
        
        return True

if __name__ == "__main__":
    solution = Solution()
    firstString = input('Enter a string and Press Enter: ')
    secondString = input('Now enter another string: ')
    if solution.isAnagram(firstString, secondString):
        print("Strings are anagrams of one another")
    else:
        print("Error: Strings are not anagrams of one another")