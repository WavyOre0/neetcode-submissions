class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        storage = []
        for char in s:
            storage.append(char)

        for char in t:
            if char in storage:
                storage.remove(char)
        if not storage:
            return True
        return False

