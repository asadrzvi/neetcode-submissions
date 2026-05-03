class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanstring = "".join([char.lower() for char in s if char.isalnum()])
        j = len(cleanstring)-1
        i = 0
        while i < j:
            if cleanstring[i] != cleanstring[j]:
                return False
            i+=1
            j-=1
        return True