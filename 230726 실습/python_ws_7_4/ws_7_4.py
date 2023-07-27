# ws_7_4.py

# 아래 클래스를 수정하시오.
class Shape:
   def __init__(self, width, height):
      self.width = width
      self.height = height


   def calculate_area(self):
      return self.width * self.height
   
   def calculate_perimeter(self):
      return 2 * self.width + 2 * self.height
   
   def print_info(self):
      print('Width:', self.width)
      print('Height:', self.height)
      print('Area:', self.width * self.height)
      print('Perimeter:', 2 * self.width + 2 * self.height)
      

shape1 = Shape(5, 3)
shape1.print_info()