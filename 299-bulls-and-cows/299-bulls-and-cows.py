class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls+=1
        s = Counter(secret)
        g = Counter(guess)
        for i in s.keys():
            if i in g.keys():
                cows+= min(s[i],g[i])
        return f"{bulls}A{cows-bulls}B"