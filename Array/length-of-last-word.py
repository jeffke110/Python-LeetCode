

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        worldList = s.split()
        return worldList[-1]

def main():
    s : str = "Hello World"
    test = Solution()
    print(test.lengthOfLastWord(s))

if __name__ == "__main__":
    main()
