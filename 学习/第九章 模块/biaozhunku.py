#标准库
import sys
#识别系统
xi= sys.platform
if xi=="win32":
    print("你的电脑是 windows系统")
print(sys.argv)
if len(sys.argv)<=1:
    print("缺少数据")
    sys.exit()#退出程序
print(sys.path)
for ko in sys.path:
    print(ko)