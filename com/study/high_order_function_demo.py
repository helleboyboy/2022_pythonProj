# encoding = utf-8

def binary_func(my_list):
    """
    普通函数实现不同的功能
        需要在内部定制对应的函数逻辑实现。
    :param my_list:
    :return:
    """

    # 内部函数
    def is_evennumber(elem):
        if elem % 2 == 0:
            return True

    def is_oddnmumber(elem):
        if elem % 2 != 0:
            return True

    def is_larger_five(elem):
        if elem > 5:
            return True

    result_list = []
    for i in my_list:
        # if is_evennumber(i):
        # if is_oddnmumber(i):
        if is_larger_five(i):
            result_list.append(i)
    return result_list


# my_list = range(1, 11)
# print(binary_func(my_list))


print("============分=================隔=======================线======================")


def is_evennumber_high(elem):
    if elem % 2 == 0:
        return True


def is_oddnmumber_high(elem):
    if elem % 2 != 0:
        return True


def is_larger_five_high(elem):
    if elem > 5:
        return True


def high_order_func(fnc, my_list):
    result_list = []
    for i in my_list:
        # if is_larger_five_high(i):
        if fnc(i):
            result_list.append(i)
    return result_list


# my_list = range(1, 11)
# print(high_order_func(is_evennumber_high, my_list))
# print(high_order_func(is_oddnmumber_high, my_list))
# print(high_order_func(is_larger_five_high, my_list))


def f1(a, b):
    return a + b


lambda a, b: a + b

# print(f1(1, 2))
# print((lambda a, b: a + b)(1, 2))


"""
匿名函数： 就是一个lambda表达式；
lambda表达式可以赋值给一个函数对象来接受，但是lambda表达式往往以匿名函数来使用
"""
my_range = range(1, 11)
print(list(filter(is_evennumber_high, my_range)))
print(list(filter(lambda i: i % 2 == 0, my_range)))
print(list(map(lambda i: i + 10, my_range)))

"""
通过参数key来改变sort函数的排序规则！
本质上也是匿名函数
"""
my_list = ['222', '13', '122222', '72', '4222', '6']
my_list.sort()
print(my_list)
my_list.sort(key=len)
print(my_list)
my_list.sort(key=int)
print(my_list)

if __name__ == '__name__':
    """
    表示代码块的内容只有在本文件执行的时候才执行，被调用不被执行！
    下面代码可以认为是 测试代码！！！
    """
    print("aaaaaaaaa")
    print("aaaaaaaaa")
    print("aaaaaaaaa")
    print("aaaaaaaaa")
    print("aaaaaaaaa")
    print("bbbbbbbb")
    print("bbbbbbbb")
    print("bbbbbbbb")
    print("bbbbbbbb")


