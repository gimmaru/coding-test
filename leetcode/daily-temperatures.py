from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        today_temp, after_temps = temperatures[0], temperatures[1:]
        for day, after_temp in enumerate(after_temps, 1):
            if today_temp < after_temp:
                return [day] + self.dailyTemperatures(after_temps)
        if after_temps:
            return [0] + self.dailyTemperatures(after_temps)
        else:
            return [0]

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for i, temp in enumerate(temperatures, 1):
            after_temps = temperatures[i:]
            flag = True
            for day, after_temp in enumerate(after_temps, 1):
                if after_temp > temp:
                    answer.append(day)
                    flag = False
                    break
            if flag:
                answer.append(0)
        return answer
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, days, answer = [], [], []

        while temperatures:
            day = 0
            temp = temperatures.pop()
            
            while stack:
                if stack[-1] <= temp:
                    stack.pop()
                    prev = days.pop()
                    if prev == 0:
                        day = 0
                    else:
                        day += prev
                else:
                    day += 1
                    break

            stack.append(temp)
            days.append(day)
            answer.append(day)

        return answer[::-1]

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)
        return answer