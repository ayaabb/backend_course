class math_operation:
    def __init__(self, num):
        self.num = num

    def is_equal(self, y):
        return self.num == y

    def is_greater(self, y):
        return self.num > y

    def is_smaller(self, y):
        return self.num < y
