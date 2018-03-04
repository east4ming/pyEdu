"""用list实现一个栈结构"""

stack = []


def push_it():
    num = input("Please input the num: ")
    stack.append(num)


def pop_it():
    if stack:
        print('\033[31;1mPoped: {}\033[0m '.format(stack.pop()))
    else:
        print('\033[31;1mEmpty stack\033[0m')


def view_it():
    print("\033[32;1m{}\033[0m".format(stack))


def show_menu():
    prompt = """(0) push_it
(1) pop_it
(2) view_it
(3) quit
Please input your choice(0/1/2/3)"""
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    while 1:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print("Invalid input, try again. ")
        if choice == '3':
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()