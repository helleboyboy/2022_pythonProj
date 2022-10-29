# -*- coding: UTF-8 -*-
from time import *


def test_equal():
    """
    == 根据value来判断是否相等
    is 根据对象的id来判断是否相等
    is not 根据对象的id来判断是否不相等
    :return:
    """
    print(1 == True)
    print(1 is True)
    print(1 is not True)


# test_equal()

"""
打印换行或者不换行
利用print的参数end来控制结束符号！默认为\n
"""


def test_print_end():
    print("aaa", end=",")
    print("aaa", end="\t")
    print("aaa", end="")
    print("bbb")
    print("ccc")


# test_print_end()

"""
九九乘法表
"""


def nine_nine_mult(count):
    # count = 9
    i = 1
    while i <= count:
        j = 1
        while j <= i:
            print(f"{j} * {i} = {i * j}", end="\t")
            j += 1
        print()
        i += 1


# nine_nine_mult(9)

"""
continue
break
break,continue均对最近的一次循环有效！！！
paas 用来占位！
"""


def test_break():
    a = 0
    while a < 10:
        a += 1
        b = 0
        while b < 10:
            b += 1
            if b == 3:
                break
            print(a, b)
        print("----一圈----")


# test_break()


def test_continue():
    c = 0
    while c < 10:
        c += 1
        d = 0
        while d < 10:
            d += 1
            if d == 3:
                continue
            print(d, d)
        print("----一圈----")


# test_continue()


def test_pass():
    a = 0
    while a <= 5:
        pass
        # print(a)
        a += 1
    print("循环结束！")


# test_pass()

"""
测试切片
切片得到的结果也是列表类型
"""


def test_qie_pian():
    a = [1, 2, 3, 4]
    result = a[1:4]
    print(result, type(result))


# test_qie_pian()


def test_in(loc_num):
    a = [1, 2, 3, 4, 5]
    if loc_num in a:
        print(loc_num)
    else:
        print("not in")


# test_in(1)
# test_in(10)


"""
:: 表示取列表的所有元素，可以通过步长来取元素
"""


def test_double_mao_hao(step):
    a = [1, 2, 3, 4, 5]
    print(a[::step])


# test_double_mao_hao(1)
# test_double_mao_hao(2)


"""
元组的解包：将元组的每一个元素都赋值给一个变量！！
应用：直接交换两个变量的值（其他语言要借助中间变量！）
"""


def test_tuple_jiebao():
    my_tuple = (1, 2, 3, 4)
    a, b, c, d = my_tuple
    print(f" a = {a}")
    print(f" b = {b}")
    print(f" c = {c}")
    print(f" d = {d}")


# test_tuple_jiebao()

"""
应用元组的解包来实现两个变量快速交换
"""


def apply_test_tuple_jiebao_jiaohuandaxiao(a, b):
    print(f"输入的a = {a}， b = {b}")
    my_tuple = (a, b)
    print(f"交换a，b的值")
    b, a = my_tuple
    print(f"交换后的的a = {a}， b = {b}")


# apply_test_tuple_jiebao_jiaohuandaxiao(1, 2)


"""
测试dict的两种获取key的方法
"""


def get_value_dict():
    my_dict = {"a": "a", "b": "b", "c": "c"}
    print(my_dict["a"])
    print(my_dict.get("a"))
    print("get not exist key ！")
    print(my_dict.get("z"))  # 返回None，不会报错
    print(my_dict["z"])  # 报错


# get_value_dict()


"""
测试删除dict的元素
del dict['key'] 也可
"""


def del_value_dict():
    my_dict = {"a": "avalue", "b": "b", "c": "c"}
    print(my_dict)
    popitem_value = my_dict.popitem()  # 删除最后一个元素，返回删除元素的kv元组
    print(popitem_value)
    print(my_dict)
    print(my_dict.pop("a"))  # 返回删除元素的value
    print(my_dict.pop("b"))  # 返回删除元素的value
    # print(my_dict.pop("z"))  # 返回不存在的key会报错
    print(my_dict.pop("z", "default"))  # 返回不存在的key会报错,可以使用默认值来规避报错
    print(my_dict.popitem())  # 无法删除空地图


# del_value_dict()


"""
测试地图的复制：浅复制 
两个地图毫无关系，但是嵌套内部的dict就是深复制了！！！
"""


def little_copy_dict():
    my_dict = {"a": "avalue", "b": "b", "c": "c"}
    second_dict = my_dict.copy()
    my_dict["a"] = "a"
    print(my_dict, id(my_dict))
    print(second_dict, id(second_dict))


# little_copy_dict()


"""
使用两个变量同时获取dict的k - v ====> items
"""


def get_k_v_dict():
    my_dict = {"a": "avalue", "b": "b", "c": "c"}
    for k in my_dict.keys():
        print(k, "==", my_dict.get(k))
    print("====")
    for v in my_dict.values():
        print(v)
    print("====")
    for k, v in my_dict.items():
        print(k, "==", v)
    print("====")


# get_k_v_dict()


"""
判断参数的类型！！！
"""


def test_panduan_type(a):
    print(type(a) == int)
    print(type(a) == str)


# test_panduan_type(11)
# test_panduan_type("11")


def test_param_jiebao(a, b, c):
    """
    方法形参的解包(元组)
    """
    print(a)
    print(b)
    print(c)


# my_tuple = (1, 2, 3)
# test_param_jiebao(my_tuple)  # 会被默认为一个形参，需要借助* 来进行解包
# test_param_jiebao(*my_tuple)


def dict_jiebao(a, b, c):
    """
    dict类型的解包需要用到两个**
    元组类型的解包需要用到一个*
    """
    print(a)
    print(b)
    print(c)


# my_tuple = {"a": 1, "b": 2, "c": 3}
# dict_jiebao(**my_tuple)
# dict_jiebao(*my_tuple.keys())
# dict_jiebao(*my_tuple.values())


def doc_guifan(a: int, b: int, c: int) -> int:
    """
    文档规范:参数里面标注的int没有强制性一定为int类型，只是指明文档要求而已！
    三个数累加
    :param a:  int类型
    :param b:  int类型
    :param c:  int类型
    :return:  int类型：sum
    """
    return a + b + c


# help(doc_guifan)


a = 0


def test_global():
    """
    测试 globa关键词 ，修改全局变量的值
    :return:
    """
    global a  # 去掉则无法改掉全局变量的值！
    a = 10
    print(a)


# test_global()
# print(a)


def know_namespace():
    """
    测试 namespace 命名空间
    namespace 在全局中获取就返回全局的命名空间，实质上就是一个dict，保存着变量的值
              在局部中获取就返回局部的明明空间（位置而定，但是可以在方法体内使用globals()来获取全局的命名空间！！！ ）
            可以直接对该dict对象操作，但是不建议
    :return: None
    """
    a = 'aaa'
    scope = locals()
    print(scope)
    print(globals())


# know_namespace()
# print(locals())


def mul(n: int) -> int:
    """
    求 n的阶乘 ： n * (n-1) * ...* 1
    :param n:
    :return:
    """
    result = n
    for i in range(1, n):
        result = result * i
    return result


# a = time()
# print(mul(500))
# b = time()
# print(b - a)


def factorial(n):
    """
     求n的阶乘 ：n * (n-1) * ...* 1
    :param n:
    :return:
    出现的问题：RecursionError: maximum recursion depth exceeded in comparison，即超出来递归的最大深度
    """
    init = n
    if init == 1:
        return 1
    return n * factorial(n - 1)


# c = time()
# print(factorial(500))
# d = time()
# print(d - c)


def power_train(base_n: int, i: int):
    """
    求任意数的i次幂
    :param base_n:
    :param i:
    :return:
    """
    if base_n == 1:
        return 1
    if base_n == 0:
        return 0
    if i == 0:
        return 1
    if i == 1:
        return base_n
    if i < 0:
        i = -i
        base_n = 1 / base_n
        power_train(base_n, i)
    return base_n * pow(base_n, i - 1)


# print(power_train(1, 3))
# print(power_train(3, 1))
# print(power_train(3, 3))
# print(power_train(3, -3))
# print(power_train(2, -3))
# print(power_train(-2, 2))
# print(1 / 27)


def huiwenshu(string):
    """
    回文数测试
    :param string:
    :return:
    """
    tmp = string
    length = len(string)
    for i in range(length):
        if i <= length / 2 + 1:
            if tmp[i] == tmp[length - i - 1]:
                continue
            else:
                return False
    return True


# train = "abcfcbaa"
# print(huiwenshu(train))


def huiwenshu_digui(string):
    if len(string) < 2:
        return True
    elif string[0] != string[-1]:
        return False
    return huiwenshu_digui(string[1:-1])


# print(huiwenshu_digui("a"))
# print(huiwenshu_digui("aba"))
# print(huiwenshu_digui("abca"))


def add(a, b):
    return a + b


def add_three(a, b, c):
    return a + b + c


def fff(fn, *args, **kwargs):
    """
    该函数对 add 函数和 add_three 函数或者更多的函数进行调用的前后做了改变。对参数不需要关注。
    该函数我们称之为 装饰器；通过装饰器，我们可以不修改原有的函数就可以进行对函数进行扩展（套多一层！）
    args和kwargs处理了不定个参数的问题！！！夺取了解！！！！！！！！！！！
    :param fn: 传入的函数对象
    :param args:
    :param kwargs:
    :return:
    """
    print("执行之前.....")
    result = fn(*args, **kwargs)
    print("执行之后.....")
    return result


@fff
def fact_decorator():
    """
    装饰器常用方法:
        普通方法的定义上方标注注解: @装饰器名
        调用普通方法即可成功调用装饰器方法了！！！！
    :return:
    """
    print("装饰器")


# # 调用装饰器 方法之一
# print(add_three(2, 3, 4))
# print("====")
# # 调用装饰器 方法之二
# print(fff(add, 1, 2))
# print("====")
# print(fff(add_three, 1, 2, 3))
# print("====")


print("-------------------")
# from high_order_function_demo import *
import high_order_function_demo as demo

print(demo)
print(demo.__name__)  # 获取demo的模块名，文件名
print(__name__)  # 获取本模块的模块名，但是由于为主方法，所以返回__main__
