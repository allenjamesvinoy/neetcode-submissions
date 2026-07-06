class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperature_stack = deque()
        day_stack = deque()

        l = len(temperatures)
        temperature_stack.append(temperatures[-1])
        day_stack.append(l-1)

        res = [0] * l
        for i in range(l-2, -1, -1):
            while temperature_stack and temperatures[i] >= temperature_stack[-1]:
                temperature_stack.pop()
                day_stack.pop()

            if temperature_stack:
                res[i] = day_stack[-1] - i

            temperature_stack.append(temperatures[i])
            day_stack.append(i)

        return res 
            