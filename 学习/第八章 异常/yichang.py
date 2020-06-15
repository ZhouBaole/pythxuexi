class yi:
    def chang():
        while True:
            try:

                f=int(input("请输入数字："))
                print(f)
                #抛异常
            except ValueError:
                print(ValueError)
            except Exception as e:
                print("未知错误：",e)
            finally:#无论是否有异常都会执行
                print("fina")
yi.chang()

