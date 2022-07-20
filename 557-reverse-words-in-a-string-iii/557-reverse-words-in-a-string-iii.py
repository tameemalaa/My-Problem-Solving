class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n =[]
        for word in words :
            word = list(word)
            i = 0
            j = len(word)-1
            while i < j :
                word[i],word[j] = word[j],word[i]
                i+=1
                j-=1
            word ="".join(word)
            n.append(word)
        return " ".join(n)