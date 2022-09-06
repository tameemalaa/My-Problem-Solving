class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        if groupSize == 1 :
            return True
        count = Counter(hand)
        s = sorted(list(count))
        while s :
            first = s[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i]==0 :
                    if i != s[0]:
                        return False
                    s.pop(0)
        return True