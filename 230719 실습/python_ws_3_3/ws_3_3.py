# ws_3_3.py
import book
number_of_book = 100

# def decrease_book(number):
    # global number_of_book
    # number_of_book -= number
    # return number_of_book



def rental_book(name, number):
    book.decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')


rental_book('홍길동', 3)
