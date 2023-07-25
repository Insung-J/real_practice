# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(a):
    b = list(reversed(a))
    c = ''.join(b)

    return c


result = reverse_string("Hello, World!")
print(result)