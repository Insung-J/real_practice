# book.py
number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book

decrease_book(3)
print(f'남은 책의 수 : {number_of_book}')