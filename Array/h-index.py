from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        for index in range(len(citations)):
            if(index >= citations[index]):
                return index
        return len(citations)