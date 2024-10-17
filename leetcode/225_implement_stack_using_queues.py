from collections import deque


class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        

    def pop(self):
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()
        

    def top(self):
        return self.q[-1]
        

    def empty(self):
        return len(self.q) == 0