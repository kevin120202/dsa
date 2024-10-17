class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x):
        while self.stack:
            self.stack2.append(self.stack.pop())
        self.stack2.append(x)
        while self.stack2:
            self.stack.append(self.stack2.pop())
        

    def pop(self):
        return self.stack.pop()
        

    def peek(self):
        return self.stack[-1]
        

    def empty(self):
        return len(self.stack) == 0