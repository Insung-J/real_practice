# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(a):
  new_tuple = ()
  new_list = []
  b = list(a)
  b.sort()

  for i in b:
    new_list.append(i)
    new_tuple = tuple(new_list)
  
  

  return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)

