"""Gen 8 password.

1. 生成8位随机密码;
2. 使用random的choice函数随机取出字符
3. 用户可以决定生成多少位密码
4. 第一个字符是: 大小写字母
5. 中间字符: 大小写字母, 数字, 特殊符号(除了空格类字符)
6. 末尾字符: 大小写字母, 数字
"""

import random
import string


def gen_passwd(length=8):
    """main func."""
    f_password = random.choice(list(string.ascii_letters))
    m_password = ''
    for i in range(length-2):
        m_password += random.choice(list(string.ascii_letters+string.digits+string.punctuation))
    l_password = random.choice(list(string.ascii_letters+string.digits))
    return f_password + m_password + l_password

if __name__ == '__main__':
    print(gen_passwd())
