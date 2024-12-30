class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.pop(self.set.index(key))

    def contains(self, key: int) -> bool:
        return key in self.set