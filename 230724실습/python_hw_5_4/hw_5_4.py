# main.py

# 아래 함수를 수정하시오.
def find_min_max(list):
    find_result = []
    list_min = min(list)
    list_max = max(list)
    find_result.append(list_min)
    find_result.append(list_max)
    find_result = tuple(find_result)
    return find_result


result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)