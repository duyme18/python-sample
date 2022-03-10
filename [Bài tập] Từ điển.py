dictionary = {
    'english': 'Tiếng Anh',
    'japanese': 'Tiếng Nhật',
    'chinese': 'Tiếng Trung',
    'vietnamese': 'Tiếng Việt'
}

def translate(dictionary_, word):
    for key in dictionary_:
        if word == key:
            print(word, ': ',dictionary_[key])
    else:
        print(word, ' not exists')

input_word = input('word: ')
translate(dictionary, input_word)