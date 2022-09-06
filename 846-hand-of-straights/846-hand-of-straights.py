class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 :
            return False
        if groupSize == 1 :
            return True
        hand.sort()
        while hand :
            prv = None
            s = set(hand)
            for i in range(groupSize-1):
                if not prv :
                    prv = hand.pop(0)
                if prv+1 in s :
                    hand.remove(prv+1)
                    prv += 1 
                else : return False
                    
        return True
                        
                        
        