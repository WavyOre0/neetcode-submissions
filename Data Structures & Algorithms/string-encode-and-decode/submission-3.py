class Solution:

    def encode(self, strs: List[str]) -> str:
        # I need to have a way know the length of each word and where to stop 
        # reading the number for the size in the output string

        res = ""
        for string in strs:
            # put size of each word, and a distinguishing char before each word
            res += str(len(string)) + "[" + string
        return res 
    def decode(self, s: str) -> List[str]:
        # want to loop over the whole string one time.
        # want to read in the size of the first to know the length
        # then you want to skip over [ to then read the word
        res= []
        i = 0
        while i < len(s):
            j = i # use another pointer that starts from i but still gets updated
            while s[j] != "[":
                j += 1
            length = int(s[i:j]) # s[j] is [
            res.append(s[j+1: j+1+ length])
            i = j+1+length
        return res
