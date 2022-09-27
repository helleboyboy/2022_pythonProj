# encoding = utf-8

class FirstClass():
    name = 'javaAndBidata'

    def javaAndBigdata_method(self):
        '''
        方法定义的时候必须存在一个形参，默认为self，否则会报错
        self即为对象本身
        :return:
        '''
        print("this is javaAndBigdata's method!!!")
        return self.name  # 表明self为对象本身

    @classmethod
    def class_method(cls):
        print("类方法，用到了 classmethod 装饰器！！")

    @staticmethod
    def static_method():
        print("静态方法，一般与类无关，常常为工具方法！！！")


javaAndBigdataInstance = FirstClass()
print(javaAndBigdataInstance.name)
print(javaAndBigdataInstance.javaAndBigdata_method())
FirstClass.class_method()
FirstClass.static_method()
