class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping character count to list of Anagrams
        for s in strs:
            count = [0] * 26 # 26 for number of lowercase letters in alphabet
            for c in s:
                count[ord(c) - ord('a')] +=1 # get the asci value of c, and subtract it by a asci val to get the correct index
            result[tuple(count)].append(s) # in the dict we grouped the anagrams together

        return list(result.values())

        #THIS IS O(m * n) m = # of strings given and n = average length of each string