class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        s = Counter(s1)
        for i in range(len(s2)-(size-1)):
            if s == Counter(s2[i:i+size]):
                return True
        return False