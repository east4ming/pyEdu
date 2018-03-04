"""记账

1. 记账时, 有10000
2. 无论开销和收入都要记账
3. 内容包括:
    - 时间
    - 金额
    - 说明
4. 永久存储
"""
import time
import pickle as p
import os


def outcome(record, wallet):
    date = time.strftime('%Y-%m-%d')
    amount = int(input("金额: "))
    comment = input('备注: ')
    with open(wallet, 'rb') as fobj:
        balance = p.load(fobj) - amount
    with open(wallet, 'wb') as fobj:
        p.dump(balance, fobj)
    with open(record, 'a') as fobj:
        fobj.write("%-15s%-8s%-8s%-10s%-20s\n" %
                   (date, amount, 'n/a', balance, comment))


def income(record, wallet):
    date = time.strftime('%Y-%m-%d')
    amount = int(input("金额: "))
    comment = input('备注: ')
    with open(wallet, 'rb') as fobj:
        balance = p.load(fobj) + amount
    with open(wallet, 'wb') as fobj:
        p.dump(balance, fobj)
    with open(record, 'a') as fobj:
        fobj.write("%-15s%-8s%-8s%-10s%-20s\n" %
                   (date, 'n/a', amount, balance, comment))


def query(record, wallet):
    with open(record) as fobj:
        for line in fobj:
            print(line, end='')
    with open(wallet, 'rb') as fobj:
        balance = p.load(fobj)
    print('当前余额是: ', balance)


def show_menu():
    record = '/tmp/record.txt'
    wallet = '/tmp/wallet.data'
    prompt = """(0): 记录开销
(1) 记录收入
(2) 查询收支记录
(3) 退出
请选择(0/1/2/3):"""
    cmds = {'0': outcome, '1': income, '2': query}
    if not os.path.exists(wallet):
        with open(wallet, 'wb') as f:
            p.dump(10000, f)
    while 1:
        try:
            choice = input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print('\nBye-bye')
            choice = '3'
        if choice not in '0123':
            print("无效输入, 请重试")
            continue
        if choice == '3':
            break
        cmds[choice](record, wallet)


if __name__ == '__main__':
    show_menu()
