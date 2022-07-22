class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s  : return 0
        str_start = 0
        mx = 1
        for str_end in range(len(s)):
            while s[str_end] in s[str_start:str_end]:
                str_start+=1
            mx= max(mx, (str_end - str_start) +1)
        return mx