def input_password():

    password = input("请输入密码:")

    if len(password) >= 8:
        return password

    # 主动抛出异常,先实例化一个Exception对象,把自定义的异常信息添加进来
    ex = Exception("密码长度不够")

    # 使用raise关键字抛出异常,在调用该函数处做异常的检测和捕获
    raise ex


try:
    print(input_password())
except Exception as result:  # result包含了异常信息
    print(result)
