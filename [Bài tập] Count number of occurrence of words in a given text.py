string = 'Hoàng hoàng Duy Nguyễn Huyền Trang CodeGym Online Python Hoàng Python'


def count_word(string_, message):
    num_words = dict()
    text_list = string_.split()

    for text in text_list:
        if text in num_words:
            num_words[text] += 1
        else:
            num_words[text] = 1

    for key, value in num_words.items():
        if message == key:
            print(key, ' : ', value)


input_message = input('input: ')
count_word(string, input_message)
