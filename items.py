class Items:

    def __init__(self):
        self.counter = 0

    def add(self):
        self.counter = self.counter + 1

    def remove(self):
        if self.counter > 0:
            self.counter = self.counter - 1

    def has_more(self):
        return self.counter > 0