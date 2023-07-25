# ws_5_5.py

# 아래 함수를 수정하시오.


def even_elements(a):
    b = []
    
    # a 길이랑 i랑 비교해서 돌때마다 i 수 올리고 비교
    i = 0
    while i < len(a):
        
        if a[i] % 2 == 1:
            a.pop(i)
            a.insert(0,None)
            i += 1
        else:
            b.extend([a[i]])
            i += 1
        
    return b
        
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)