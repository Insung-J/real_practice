# ws_4_3.py

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

    # # 응답 데이터 출력
    # print(response)

    # # 변환 데이터 출력
    # print(parsed_data)
    # # 변환 데이터의 타입
    # print(type(parsed_data))

    # # 특정 데이터 출력
    # print(parsed_data['name'])
    # print(parsed_data['username'])
    # print(parsed_data['company']['name'])
    
    # 변환데이터의 'name'을 리스트로 추가하면서 저장
    dummy_dict = {}
    dummy_dict['company'] = parsed_data['company']['name']
    dummy_dict['lat'] = parsed_data['address']['geo']['lat']
    dummy_dict['lng'] = parsed_data['address']['geo']['lng']
    dummy_dict['name'] = parsed_data['name']

    if ((float(dummy_dict['lat']) >= (80)) or
        (float(dummy_dict['lat']) <= (-80)) or
        (float(dummy_dict['lng']) >= (80)) or
        (float(dummy_dict['lng']) <= (-80))
        ):
        continue

    dummy_data.append(dummy_dict)

    # print(dummy_dict)

    # dummy_data.append(parsed_data['company']['name'])

print(dummy_data)
# print(dummy_dict)