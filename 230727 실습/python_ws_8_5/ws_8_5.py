# ws_8_5.py
class Animal:
   num_of_animal = 0
   def __init__(self):
      Animal.num_of_animal += 1


class Dog(Animal):
   sound = '멍멍' #속성


class Cat(Animal):
   sound = '야옹' #속성


class Pet(Cat, Dog):

    def __str__(self):
       return print(f'애완동물은 {self.sound}소리를 냅니다.')
       


pet1 = Pet()
pet1.__str__()

