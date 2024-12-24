###
private access modifiers
###
class A:
    def __init__(self,name):
        self.__name = name
a = A("deepika")
print(a._A__name)
###
deepika
