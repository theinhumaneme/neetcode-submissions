class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        word3 = ""
        while i < len(word1) and j < len(word2):
            word3 += word1[i]
            word3 += word2[j]
            i += 1
            j += 1
        if i < len(word1):
            word3 += word1[i : len(word1)]
        if j < len(word2):
            word3 += word2[i : len(word2)]
        return word3