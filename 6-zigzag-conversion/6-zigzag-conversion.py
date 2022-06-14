class Solution:
    def convert(self, s: str, numRows: int) -> str:
        aux_str = ["" for i in range(numRows)]
        
        
        i = 0
        while i < len(s):
            for j in range(numRows):
                aux_str[j]+= s[i]
                i+=1
                if i >= len(s):
                    return "".join(aux_str)
            for j in range(numRows-2,0,-1):
                aux_str[j]+=s[i]
                i+=1
                if i >= len(s):
                    return "".join(aux_str)