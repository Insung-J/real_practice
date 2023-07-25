def even_elements(a):
    result = []
    while len(a) != 0:
        element = a.pop(0)
        if element % 2 == 0:
            result.extend([element])
    return result



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)