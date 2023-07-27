class list:
    def append(self, arg):
        #self에 요소 하나를 추가하는 동작


        a = [1, 2, 3]

# 인스턴스.인스턴스메서드
        a.append(4)  # 축약형이므로 append(a, 4) 이렇게 안쓴다


# 파이썬이 이해하는 코드
        list.append(a, 4) # 위에 코드랑 같은 코드이다..