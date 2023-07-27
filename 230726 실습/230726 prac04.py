
class Person:
    #  속성(클래스 변수)
    count = 0 # 생성되면서 자동으로 해야되는 로직이 있다면 여기서 적을 수 있음
    def __init__(self, name):
        self.name = name # 여기서 self.name 이거 많이 까먹음!!! 왜인지도 모르겠다..
        self.ssafy = name # ssafy는 그냥 인스턴스 변수 이름일 뿐이고 == 뒤에 name이 값이다. 굳이 다르게 할 필욘 없다


    # 인스턴스 메서드
    def instance_method(self):
        self.인스턴스변수

    # 클래스메서드
    @classmethod
    def class_method(cls):
        cls.클래스변수
        cls.클래스메서드

        cls.count += 1

    # 스태틱메서드
    @staticmethod
    def static_method(a, b):
        return a + b

    # 인스턴스 생성
    인스턴스 = 클래스() # 괄호안에는 생성자함수에 따라 달라짐?

    # 인스턴스 변수 설정
    인스턴스.변수 = 값 # 이건 클래스,다른인스턴스에 영향없고 저 인스턴스에만 영향있음

    # 인스턴스 메서드 사용(호출)
    인스턴스.인스턴스메서드()

