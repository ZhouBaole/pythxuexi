class pl:
    #类变量
    ll=9
    #默认执行__init__ 方法第一个参数必须为 self（公用）
    def __init__(self,name):
        print(name)
        self.name=name
        self.__name=name#私有属性
        print("这是我私有的",self.__name)
        return
    def play(self):
        print("pl.play():",self.name)
        return
    #私有方法
    def __play(self):
        print("pl.play():", self.name)
        return
#继承
print("--------------------继承------------------")
class ko(pl):
    def l(self):
        super(ko,self).__init__("ji")
        print(self.name)
kl=ko("asd")
kl.play()
kl.l()
kl.play()
#多态#子类与父类有相同的方法运行调用的是子类的方法
print("-----------------多态--------------------")
class duo(pl):
    def __init__(self, name):
        print("duo",name)
        self.name = name
        self.__name = name  # 私有属性
        print("duo这是我私有的", self.__name)
        return
    def play(self):
        print("duo")
ji=duo("sdf")
ji.play()
print("类变量：",pl.ll)

class jing:
    name="dasd"
    # 定义静态类()
    @staticmethod
    def play(d):
        print("静态类：",d)
    #类方法
    @classmethod
    def lei(cls):
        print("类",cls.name)
jing.play("asd")
jing.lei()

