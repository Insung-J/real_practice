# 0-9 요소를 가지는 리스트 만들기

# 1. 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 ==1:
        new_list.append(i)
    else:
        new_list.append(str(i))
print(new_list)

# 2. list comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1]
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
print(new_list_2)
print(new_list_3)