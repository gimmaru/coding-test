import sys

sys.stdin = open("input.txt", "r")


class Solution:
    total = sys.maxsize

    @classmethod
    def solution(self, C, weights):
        if self.total < C - sum(weights):
            return self.total

        if not weights or C == 0:
            return C

        w = weights.pop()

        if C - w > 0:
            # 현재 w를 더한 것
            a = self.solution(C - w, weights.copy())
        else:
            a = C

        # 현재 w를 더하지 않은 것
        b = self.solution(C, weights.copy())
        
        self.total = min(a if a < b else b, self.total)
        return self.total
    

if __name__ == "__main__":
    C, N = map(int, input().split())
    weights = [int(input()) for _ in range(N)]

    print(f"{C - Solution.solution(C, weights)}\n\n")