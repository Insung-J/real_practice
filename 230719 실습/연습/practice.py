from my_package.math import my_math

print(my_math.pi)

print(my_math.add(100,200))

import requests

response = requests.get('https://dog.ceo/api/breeds/image/random')

print(response.json())