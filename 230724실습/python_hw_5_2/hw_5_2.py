# main.py

# 아래 함수를 수정하시오.
def count_character(a,c):
    b = list(a).count(c)
    return b
result = count_character("Hello, World!", "o")
print(result) # 2