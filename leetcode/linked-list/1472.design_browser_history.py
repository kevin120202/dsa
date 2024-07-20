class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage):
        self.curr = Node(homepage)

    def visit(self, url):
        new_node = Node(url, self.curr)
        self.curr.next = new_node
        self.curr = self.curr.next

    def back(self, steps):
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.value

    def forward(self, steps):
        counter = 0
        while self.curr.next and counter < steps:
            self.curr = self.curr.next
            counter += 1
        return self.curr.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
