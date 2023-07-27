class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1
  

class Dog(Animal):
   def __init__(self):
      super().__init__()

   def bark(self):
      print('멍멍!')


class Cat(Animal):
   def __init__(self):
      super().__init__()

   def meow(self):
      print('야옹!')


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        return cls.num_of_animal
    
    def __init__(self, sound):
       self.sound = sound
       super().__init__()
       

    def play(self):
       print('애완동물과 놀기')

    def make_sound(self):
       print(self.sound)
    




pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
