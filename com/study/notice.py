# -*- coding: UTF-8 -*-


"""
# == 根据value来判断是否相等
# is 根据对象的id来判断是否相等
# is not 根据对象的id来判断是否不相等
"""


def test_equal():
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
