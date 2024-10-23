class Solution(object):
    def carFleet(self, target, position, speed):
        stack = []
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True, key=lambda x: x[0])

        for car in cars:
            pos, spd = car
            time = float((target - pos)) / spd
            if not stack or stack[-1] < time:
                stack.append(time)
                
        return len(stack)