class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool: 
        l = len(hand)
        if l % groupSize != 0: 
            return False

        count = defaultdict(int)
        for card in hand:
            count[card] += 1

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            top = min_heap[0]

            for i in range(top, top + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if min_heap[0] != i:
                        return False
                    heapq.heappop(min_heap)

        return True

                

