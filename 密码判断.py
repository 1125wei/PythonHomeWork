"""

判断密码强度

"""

from tqdm import tqdm  # 引入tqdm包用于进度条功能

import time  # 引入time包，配合进度条功能进行程序执行

import re  # 引入re包执行内容字符串检查


def JudgmentCode(code: str) -> str:  # 接收password内容，并返回字符串

    weak = "弱，建议改进"  # 提前设置"weak""middle""strong"三个变量

    middle = "中，可进一步提升"

    strong = "强，密码安全"

    count = 0  # 计数器，根据计数器大小判断密码强度

    if len(code) <= 8:
        return weak  # 如果长度小于8直接返回弱，不再进行之后判断

    if re.search("[a-z]", code) or re.search("[A-Z]", code):
        count += 1  # 如果密码内有字母a-z或者A-Z，计数器加一

    if re.search("[0-9]", code):
        count += 1  # 如果密码内有0-9，计数器加一

    if re.search("[-+=?/.,;:'|}{!@#$%&_*~]", code):
        count += 1  # 如果密码内有"!@#$%&_*~"等特殊字符计数器加一

    # 根据计数器count大小选择返回值

    if count == 3 and code[0].istitle() and len(code) >= 16:  # 检查密码是否包含特殊字符以及是否已大写字母开头，和密码长度是否>=16
        return strong
    elif count >= 2:  # 只要count大于等于2，就返回middle，因为至少包含了两类字符
        return middle
    else:
        return weak  # 如果count小于2，返回weak


if __name__ == '__main__':  # main方法，程序执行入口

    password = input("输入密码:")  # 输入需要判断密码，赋值给password

    print("正在进行密码强度判断")

    for i in tqdm(range(1, 101)):  # 执行100次循环，每次循环0.01秒，用于执行进度条，实际情况下会拖慢程序执行速度，影响程序执行效率

        time.sleep(0.01)

    print("你的密码强度为:" + JudgmentCode(password))  # 输出判断结果
