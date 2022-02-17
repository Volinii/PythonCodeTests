from abc import abstractmethod, ABCMeta, abstractclassmethod

class A:
    @abstractmethod
    def hi(self):pass

class B(A):
    def tt(self):
        print(1)
a=A()
b=B()
b.hi()