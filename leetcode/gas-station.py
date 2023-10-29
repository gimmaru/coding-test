from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, curr = 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            if curr <= 0:
                curr = 0
                answer = i
            
            state = g - c
            curr += state
            total += state

        return answer if total >= 0 else -1


# 답지 풀이
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start