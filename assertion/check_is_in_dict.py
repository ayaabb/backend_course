class assert_dict:
    def __init__(self, value):
        self.value = value

    def is_key(self, dictionary):
        if isinstance(dictionary,dict) :
            if self.value in dictionary.keys():
                 return True
        else:
            if self.value == dictionary:
                return True
        for value in dictionary.values():
            if isinstance(value, dict):
                if self.is_key(self.value):
                    return True
        return False

    def is_value(self, dictionary):
        for val in dictionary.values():
            if val == self.value:
                return True
            elif isinstance(val, dict):
                if self.is_value(val):
                    return True
        return False
