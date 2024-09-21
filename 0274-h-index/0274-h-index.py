class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h_index = 0
        for i in range(0,len(citations)):
            if citations[i]>= i+1:
                h_index = i+1
            else: 
                continue

        return h_index

            