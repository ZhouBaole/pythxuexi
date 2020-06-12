'''

                                          4.1.1索引

'''   
print("-----------索引------------")
#列表
x1=[1,2,3,4,5]
print("列表")
print(x1[0])
print(x1[-1])
#元组
x2=(1,2,3,4,5)
print("元组")
print(x2[0])
print(x2[1])


'''

                                          4.1.2切片

'''   
print("-----------切片------------")
#列表
print("列表")
print(x1[:])
print(x1[0:3])
print(x1[1:5])
#元组
print("元组")
print(x2[:])
print(x2[0:3])
print(x2[1:4])
#字符串
print("字符串")
x3="12345"
print(x3[:])
print(x3[0:3])
print(x3[1:4])
print("----------------------")
#获取非连续的序列
#列表
print("列表")
print(x1[1:5:2])
#元组
print("元组")
print(x2[1:4:2])
#字符串
print("字符串")
print(x3[1:4:2])