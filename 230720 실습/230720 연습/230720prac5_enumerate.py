result = ['a', 'b', 'c']

print(enumerate(result)) # <enumerate object at 0x000001BF8B649140>
print(list(enumerate(result))) # [(0, 'a'), (1, 'b'), (2, 'c')]

for index, elem in enumerate(result):
    print(index, elem)
"""
0 a
1 b
2 c
"""


