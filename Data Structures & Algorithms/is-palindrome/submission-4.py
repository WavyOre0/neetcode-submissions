class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "")
        l,r = 0, len(string) -1
        while l < r:
            if not string[l].isalnum():
                l += 1
            elif not string[r].isalnum():
                r -= 1
            elif string[l].lower() != string[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
