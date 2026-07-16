class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)
        sum_cost = sum(cost)
        
        if sum_gas < sum_cost:
            return -1

        cumm = 0
        res = 0

        for i in range(len(gas)):
            cumm += (gas[i] - cost[i])

            if cumm < 0:
                cumm = 0
                res = i + 1
        
        return res