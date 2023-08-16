from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) < 1:
            return ""
        cmpstr : str = strs[0]

        for index in range(1, len(strs)):

            element = strs[index]
            charIndex = 0
            while(charIndex < len(cmpstr) and charIndex < len(element) and 
                    cmpstr[charIndex] == element[charIndex] ):
                charIndex += 1


            if charIndex < len(cmpstr):
                cmpstr = cmpstr[:charIndex]
            elif charIndex < len(element):
                cmpstr = element[:charIndex]

        return cmpstr
            
