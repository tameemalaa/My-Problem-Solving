class Solution:
    def isHappy(self, n: int) -> bool:
        s= set()
        while n not in s:
            holder = 0
            s.add(n)
            for i in str(n):
                holder += int(i)**2
            n = holder
            if n ==1 : return True
        return False