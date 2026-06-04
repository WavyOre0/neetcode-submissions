class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        res = 0
        for l,char in enumerate(s):
            r = l + 1
            counter = 1
            stor = set()
            stor.add(char)
            while r < len(s) and s[r] not in stor:
                counter+=1
                stor.add(s[r])
                r +=1
            res = max(res, counter)
        return res
                
