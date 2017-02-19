class base_register(type):

    def __new__(cls, name, bases, clsdict):
        registry = 0
        print('--------------')
        print(cls, name, bases)
        clsobj = super().__new__(cls, name, bases, clsdict)
        a = setattr(clsobj, )
        # registry += 1
        print(a)
        print(registry)
        print(clsobj)
        print('--------------')
        return clsobj


class Base(metaclass=base_register):
    count_inst = 0

    def __init__(self):
        self.__class__.count_inst += 1


class A(Base):
    pass


class B(Base):
    pass


class C(A, B):
    pass

b1 = Base()
b2 = Base()
a1 = A()
a2 = A()
print(Base.count_inst)
