class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = {jewel: 0 for jewel in set(jewels)}
        result = 0
        for stone in stones:
            if stone in jewel_dict:
                result += 1
        return result
