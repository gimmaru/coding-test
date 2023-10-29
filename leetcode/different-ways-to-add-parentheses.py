from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        results = []
        for idx, op in enumerate(expression):
            if op in {'*', '+', '-'}:
                lefts = self.diffWaysToCompute(expression[:idx])
                rights = self.diffWaysToCompute(expression[idx+1:])

                for left in lefts:
                    for right in rights:
                        results.append(eval(f"{left}{op}{right}"))
        return results


# 답지 풀이
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "*+-":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index+1:])

                results += compute(left, right, value)
        return results