
import book 

number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    user_dict = {'name' : name, 'age' : age, 'address' : address}
    print(f'{name}님 환영합니다!')

    return user_dict

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

#유저 목록
user_list = list(map(create_user, name, age, address))

# address 가 안쓰이면 어떻게 제외..? -> 무시해도 됨

def make_new_user_list(user_info):
    result = {
        'name' : user_info['name'] ,
        'age' : user_info['age'] // 10
    }
    return result

new_user_list = list(map(make_new_user_list, user_list))


# many_user = None

# 렌탈이 진행되는 함수
def rental_book(user_info):
    # 남의 책의 수 계산
    book.decrease_book(user_info['age'])
    print(f'{user_info["name"]}님이 {user_info["age"]}권의 책을 대여하였습니다.')


list(map(rental_book, new_user_list))