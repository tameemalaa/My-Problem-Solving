class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = dict()
        for i in range(len(s)):
            if s[i] in mp.keys():
                if mp[s[i]] != t[i]:
                    return False
            elif t[i] in mp.values():
                return False
            else : mp[s[i]] = t[i]
        return True