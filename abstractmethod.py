###
write a program  for abstract method?
###
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def f1(self):
        pass
class B(A):
    def f1(self):
        print('class b is abstract method')
b1 = B()
b1.f1()
###
class b is abstract method
