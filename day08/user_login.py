"""使用字典模拟一个用户登陆信息系统

1. 支持新用户注册, 新用户名和密码注册到字典中
2. 支持老虎用户登陆, 用户名和密码正确提示登陆成功
3. 主程序通过循环询问什么操作, 根据用户的选择, 执行注册或是登陆操作
"""


import getpass

user_info = {}


def logup():
    while 1:
        username = input("请输入要注册的用户名: ")
        if username in user_info:
            print("\033[31;1m用户名已经存在, 请重新输入:\033[0m")
            continue
        break
    # password = input("请输入对应的密码")
    password = getpass.getpass("请输入对应的密码:")
    user_info[username] = password
    print("\033[32;1m用户名'{}'已经注册成功\033[0m".format(username))


def login():
    n = 3
    while n:
        username = input("请输入要登陆的用户名: ")
        # password = input("请输入对应的密码: ")
        password = getpass.getpass('请输入对应密码:')
        n -= 1
        if password != user_info.get(username):
            print("\033[31;1m用户名或密码输入错误, 请重新输入\033[0m")
            continue
        print("\033[32;1m恭喜, 登陆成功\033[0m")
        break
    else:
        print("\033[31;1m输入错误超过3次, 登陆失败\033[0m")


def oper_ui():
    prompt = """1: 注册
2: 登陆
3: 退出
请问要进行那个操作(1/2/3)?"""
    cmds = {'1': logup, '2': login}
    while 1:
        choice = input(prompt).strip()[0]
        if choice not in '123':
            print("非法输入, 请重新输入")
            continue
        if choice == '3':
            break
        cmds[choice]()


if __name__ == '__main__':
    oper_ui()
