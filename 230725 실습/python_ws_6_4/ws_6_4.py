# ws_6_4.py

# 아래 함수를 수정하시오.
def get_keys_from_dict(a):
    b = a.keys()
    c = list(b)
    return c

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)