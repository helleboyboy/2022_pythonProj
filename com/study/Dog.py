# encoding = utf-8

class Dog:
    """
    __init__类似这种双下划线开头且结尾的方法为特殊方法，可以看成初始化方法或者是Java的构造器
    get_属性名 、 set_属性名 为属性增加对应的getter 方法和 setter方法，即提供读、改权限
    _属性名 : 含义就是不希望你去修改该值，一般为建议的形式为: _形参名
    不建议直接操作属性，而是通过调用getter 方法和 setter方法来操作

    """

    def __init__(self, name, age):
        print("__init__ method ")
        print("初始化的作用")
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


dog = Dog('小黄', 11)
dog.set_name('小黑')
dog.set_age(10)
print(dog.get_name())
print(dog.get_age())

