###
protected access modifiers
###
class Sample:
    def __init__(self,name):
        self._protected_member = name
m = Sample('palle')
print(m._protected_member)
###
palle
