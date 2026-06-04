class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Check, s2Check = {}, {}
        if len(s1) > len(s2): return False

        for i, char in enumerate(s1):
            s1Check[char] = 1 + s1Check.get(char, 0)
            s2Check[s2[i]] = 1 + s2Check.get(s2[i], 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if s1Check == s2Check:
                return True
            char = s2[l]
            s2Check[char] -=1
            if s2Check[char] == 0:
                del s2Check[char] 
            l += 1
            s2Check[s2[r]] = 1 + s2Check.get(s2[r], 0)
        if s1Check == s2Check:
            return True
        return False


        