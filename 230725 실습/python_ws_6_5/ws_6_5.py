# ws_6_5.py

# 아래 함수를 수정하시오.
def difference_sets(a, b):
    c = a.difference(b)
    return c
result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)