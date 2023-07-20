# 리스트를 생성하는 3가지 방법 비교
# 어떤게 제일 빨라요??
# 정수 1, 2, 3을 가지는 새로운 리스트 만들기

numbers = ['1', '2', '3']

# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers) #[1, 2, 3]

# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2)

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers ]
print(new_numbers_3)


