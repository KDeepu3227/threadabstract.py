###
create a abstract class with an abstract method m1 and complete method m2 acces both those method?
###
class A(ABC):
    @abstractmethod
    def m1(self):
        pass
    def m1(self):
        print('hi')
class B(A):
    def m2(self):
        print('hello python')
b1 = B()
b1.m1()
b1.m2()
###
hi
hello python
