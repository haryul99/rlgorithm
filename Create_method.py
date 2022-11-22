class Animal() :

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("먹는다")
    def walk(self):
        print("걷는다")
        
    def greet(self):
        print("{}가 인사한다".format(self.name))
        
class Human(Animal):

    def __init__(self, name, age, hand):
        super().__init__(name, age)
        self.hand = hand

    def wave(self):
        print("{}손을 흔들면서".format(self.hand), end=' ')
        
    def introduce(self):
        print("나이는 {}살 입니다.".format(self.age))
        
    def greet(self):
        self.wave()
        super().greet()
        
person = Human("하률이",23,"왼")

person.greet()
person.introduce()


# 내가 정의하는 ExceptionError

class MymakeExceptionError(Exception):
    '''직접 만든 ExceptionError'''