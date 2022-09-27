# encoding = utf-8

class A():

    def __init__(self, name, age):
        print("a 类 init method")
        print(f"name={name}")
        print(f"age={age}")
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def a_method(self, name):
        print(f"a 类的方法, 参数为 {name}")


def b_method():
    print("b 的普通方法")


class B(A):
    def __len__(self):
        return 20

    def __init__(self, score):
        print(super())
        super(B, self).__init__("aaa", 111)
        print("b类的init method")
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def a_method(self, name):
        print(f"这是b类的a方法，已经重写，参数为{name}")


class C:
    pass


b = B(100)
print(B.__bases__)
print(b.score)
b.name = 'b_name'
b.a_method(b.name)
b_method()


def say_hello(obj):
    # 类型检查！
    if isinstance(obj, A):
        print(f"hello, {obj.name} ~ ~ ~")


say_hello(b)
say_hello(A('小A', 11))
say_hello(C())
# len方法默认为类中的__len__方法
print(len(b))
