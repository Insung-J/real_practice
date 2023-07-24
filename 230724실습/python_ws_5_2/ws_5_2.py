# ws_5_2.py

# 아래 함수를 수정하시오.
def remove_duplicates(a):
    new_lst = []
    b = set(a)
    for i in b:
        new_lst.append(i)

    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)