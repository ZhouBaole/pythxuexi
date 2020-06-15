import os#OS封装了操作系统的文件和目录操作
"""
获取当前文件所在目录
"""
print(__file__)#获取当前文件的位置,精确到文件名
print(os.path.dirname(__file__))#获取当前文件的位置,精确到父文件夹
"""
获取当前文件的路径以及切换当前路径
"""
print(os.getcwd())#获取当前执行程序路径
os.chdir(r"F:\Python\ID\学习\venv\方法")#修改路径
print(os.getcwd())
"""
重命名文件
"""
#os.rename("F:/Python/ID/学习/venv/第九章 模块/Os.py","F:/Python/ID/学习/venv/第九章 模块/OS.py")
#rename函数可以重命名文件
'''
查看指定路径是否存在
'''
path=os.path.exists("F:/Python/ID/学习/venv/第九章 模块/fla.py")
if path:
    print("存在已修改")
    os.rename("F:/Python/ID/学习/venv/第九章 模块/fla.py", "F:/Python/ID/学习/venv/第九章 模块/flas.py")
else:
    print("不存在已修改")
    os.rename("F:/Python/ID/学习/venv/第九章 模块/flas.py", "F:/Python/ID/学习/venv/第九章 模块/fla.py")
'''
判断路径是否是一个文件
'''
pthfl=os.path.isfile("F:/Python/ID/学习/venv/第九章 模块/flb.py")
if pthfl:
    print("是一个文件")
else:
    print("不是一个文件")
'''
判断是否是一个目录
'''
mul=os.path.isdir("F:/Python/ID/学习/venv/第九章 模块")
if mul:
    print("是一个目录")
else:
    print("不是一个目录")

'''
获取系统环境变量
'''
for k,v in os.environ.items():
    print(k,":",v)
'''
创建单层目录
'''
#os.mkdir(r"F:\Python\ID\学习\venv\第九章 模块\单层测试3")
'''
创建多层目录
'''
#os.makedirs(r"F:\Python\ID\学习\venv\第九章 模块\多层测试1\1\1")
