class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        final = ""
        for _ in s:
            if _.isalnum():
                final += _
        i = 0
        j = len(final)-1
        print(final)
        while i<=j:
            if final[i] == final[j]:
                i = i+1
                j = j-1
            else:
                return False
        return True