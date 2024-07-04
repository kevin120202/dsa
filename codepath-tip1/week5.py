class Pokemon():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp  # hit points
        self.damage = damage  # The amount of damage this pokemon does to its opponent every attack

    def attack(self, opponent):
        if opponent.damage - self.hp == 0:
            return f""
