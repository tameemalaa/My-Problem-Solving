class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def isub(str1,str2):
            if str1 == '':
                return True
            if str2 == '':
                return False 
            if str1[0] == str2[0] :
                return isub(str1[1:],str2[1:])
            else :
                return isub(str1,str2[1:])
        return isub(s,t)