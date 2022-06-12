
class RAM():
    def __init__(self, size):
        self.size = size
        self.data = [0] * size
        self.used = 0
    def put(self, data):
        if self.used < self.size:
            self.data[self.used] = data
            self.used += 1
            return True
        else:
            return False
    def get(self):
        if self.used > 0:
            self.used -= 1
            return self.data[self.used]
        else:
            return None
    def check(self):
        return self.used
