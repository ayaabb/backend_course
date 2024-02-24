class code_deciphers:
    def __init__(self, my_text, keys):
        self.my_text = my_text
        self.keys = keys
        self.len_keys = len(keys)
        self.len_text = len(my_text)
        self.curr_index_keys = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.curr_index_keys < self.len_keys and self.keys[self.curr_index_keys] >= self.len_text:
            self.curr_index_keys += 1

        if self.curr_index_keys >= self.len_keys:
            raise StopIteration
        value = self.my_text[self.keys[self.curr_index_keys]][0]
        self.curr_index_keys += 1
        return value


def generate_keys(text, message):
    for m in message:
        for i in range(len(text)):
            if text[i][0] == m:
                yield i
                break



# I implemented another generator for keys in another way,I implemented two generators because I don't know if it's clever to use break after yield..
#  I don't know which way is better or more efficient , I would be glad if you could tell me that :)

# def find_index(text, char):
#     for i in range(len(text)):
#         if text[i][0] == char:
#             yield i
#
#
# def generate_keys(text, message):
#     for m in message:
#         yield next(find_index(text, m))


if __name__ == '__main__':
    my_text1 = open("MyText1.txt", "r")
    my_text1 = my_text1.read()
    keys1 = [4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100, 30, 10, 26, 16, 29, 155, 32,
             37, 61, 15, 42, 3, 633, 27, 70, 77, 45, 55, 43, 35, 108, 103, 56, 159, 166, 7, 8, 174, 36]
    my_text1 = my_text1.replace('.', '')
    my_text1 = my_text1.replace(',', '')
    my_text1 = my_text1.replace('-', '')
    my_text1 = my_text1.replace(';', '')
    my_text1 = my_text1.replace(':', '')
    my_text1 = my_text1.split()

    my_code_decriptor = code_deciphers(my_text1, keys1)
    message = ""
    for char in my_code_decriptor:
        message += char
    print(f'my first text message is :{message}')

    keys_list_generated = generate_keys(my_text1, message)
    key_list = []
    for key in keys_list_generated:
        key_list.append(key)
    print(f'The generated key list of the "{message}" and the text file is : {key_list}')
