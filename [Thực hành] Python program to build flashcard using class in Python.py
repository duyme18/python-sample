import random


class Flashcard:
    def __init__(self):
        self.animals = {'Con ong': 'bee',
                        'Con thỏ': 'rabbit',
                        'Con cua': 'crab',
                        'Con mèo': 'cat',
                        'Con ngựa': 'horse',
                        'Con khỉ': 'monkey',
                        'Con lừa': 'donkey'}

    def quiz(self):
        while True:
            vietnamese, english = random.choice(list(self.animals.items()))
            print("Tiếng Anh của '{}' là: ".format(vietnamese))
            user_answer = input()

            if user_answer.lower() == english:
                print("Đúng")
            else:
                print("Sai")

            option = int(input("Nhập 0 để tiếp tục : "))
            if option:
                break
        print("Kết thúc")


fc = Flashcard()
fc.quiz()
