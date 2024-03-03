class assert_list:
    def __init__(self, value):
        self.value = value

    def in_list(self, nested_list):
        if isinstance(self.value, list):
            if self.value == nested_list:
                return True
            if len(nested_list) == 0 and len(self.value) == 0:
                return True
        for val in nested_list:
            if val == self.value:
                return True
            elif isinstance(val, list):
                if self.in_list(val):
                    return True
        return False
