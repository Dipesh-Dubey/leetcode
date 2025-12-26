class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        else:
            gas_avail = 0
            res = 0
            for i in range(len(gas)):
                gas_avail = gas_avail + gas[i] - cost[i]

                if gas_avail<0:
                    gas_avail = 0
                    res = i+1                
                
            return res
                    