import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    

    # 문제에서 요구하는 딕셔너리 만들기
    user_info = {
        'name' : parsed_data['name'],
        'lat' : parsed_data['address']['geo']['lat'],
        'lng' : parsed_data['address']['geo']['lng'],
        'company' : parsed_data['company']['name']
         }
    
    # 위도와 경도가 특정 조건을 만족한다면..
    if ((float(user_info['lat']) >= (80)) or
        (float(user_info['lat']) <= (-80)) or
        (float(user_info['lng']) >= (80)) or
        (float(user_info['lng']) <= (-80))
        ):
        continue

    dummy_data.append(user_info)

# print(dummy_data)

black_list = ['Hoeger LLC', 
              'Keebler LLC', 
              'Yost and Sons', 
              'Johns Group', 
              'Romaguera-Crona']


# 블랙리스트 포함 여부에 따라 T/F를 반환하는 함수
def censorship(data):
    # 회사 명이 블랙 리스트에 있다면,
    # ~ 소속의 ~는 등록할 수 없습니다를 출력하고 False를 반환한다.
    if data['company'] in black_list:
        print(f'{data["company"]}의 {data["name"]} 은/는 등록할 수 없습니다.')
        return False
    # 블랙 리스트에 포함되어 있지 않다면,
    else:
        print('이상 없습니다')
        return True
    

def create_user(dummy_data):
    censored_user_list = {}
    for data in dummy_data:
        if censorship(data) is True:
            censored_user_list[data['company']] = [data['name']]

    return censored_user_list

print(create_user(dummy_data))