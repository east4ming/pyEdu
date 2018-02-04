"""创建用户.

1. 实现创建用户功能
2. 提示输入用户名
3. 随机生成8位密码
4. 创建用户并设置密码
5. 将用户相关信息写入指定文件

subprocess.call('ls', shell=True) -> int
"""
import sys
import subprocess

import gen_passwd


def add_user(username, passwd, file):
    user_info = """User Info:
    username={}
    password={}
"""
    subprocess.call('useradd {}'.format(username), shell=True)
    subprocess.call('echo {} | passwd --stdin {}'.format(passwd, username), shell=True)
    # subprocess.call('passwd --stdin {} < (echo {})'.format(username, passwd), shell=True)
    with open(file, 'a') as f:
        f.write(user_info.format(username, passwd))


if __name__ == '__main__':
    username = sys.argv[1]
    passwd = gen_passwd.gen_passwd()
    file = 'security.properties'
    add_user(username, passwd, file)
