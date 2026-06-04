class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        thing = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            thing[key].append(s)
        return list(thing.values())        