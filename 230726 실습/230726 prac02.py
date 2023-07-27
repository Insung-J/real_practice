# Person 정의
class Person:
    name = 'unknown' # 클래스속성, 클래스 변수

    # 인스턴스 메서드 (이거 사용을 인스턴스가 하기 때문임)
    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() #unknown  # 인스턴스 변수가 부여된게 아니지만 클래스에 있는걸 찾아감



# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()
p2.name = 'Kim'
p2.talk()

print(Person.name)
print(p1.name)
print(p2.name)


