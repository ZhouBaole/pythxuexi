#函数
#必须参数，传参数是顺序要保持一致
print("------------必须参数-------------")
def hu(a,b):
    print(a,"+",b,"=",a+b)
    return a+b
v=hu(2,7)
print("和为",v)
#关键字参数，可以引用的时候不按照参数的顺序
print("------------关键字参数-------------")
def guan(name,age):
    print("名字:",name,"\n年龄:",age)
guan(age=3,name="asd")
#默认参数，没有传值函数就是用默认值
print("------------默认参数-------------")
def guadn(name,age=9):
    print("名字:",name,"\n年龄:",age)
guadn(name="asd")
#可变参数   *args:参数，获取的是一个元组；**kwargs:参数，获取的是一个字典
print("------------可变参数-------------")
def args(*args):
    print("*args:",args)
args(1,2)
def kwargs(**kwargs):
    print("**kwargs:",kwargs)
kwargs(j=2,l="p")
              #*args和**kwargs结合使用
j=0
def kargss(*args,**kwargs):
    """
    asdlk 
    asdasd
    asd
    asdasdasd
    asdasd
    """
    global j
    for k in args:
        j+=k
    print("总和为：",j)
    for k,v in kwargs.items():
        print(k,":",v)
    return
kargss(1,2,3,4,姓名="asdasd",年龄=987)
l=[1,23,34]
t={"姓名":"asdasd2","年龄":9872}
kargss(*l,**t)
print(kargss.__doc__)#文档字符串
print(help(kargss))
#lambda 匿名函数
a=3
b=9
ba=lambda a,b:a*b
print(a,"*",b,"=",ba)
print(a,"*",b,"=",ba(a,b))
#函数注释
def ko(l:"sdasdasd",d:"asdasd")->int:
    pass
    return
print(ko.__annotations__) 


