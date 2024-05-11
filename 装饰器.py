import time
import socket
import sys
import os


def journal(fun):
    """
    :param fun: 给函数添加日志信息装饰器
    :return: wrapper
    """

    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        hostname = socket.gethostname()
        process_full_name = sys.argv[0]
        process_name = os.path.basename(process_full_name)
        # 获取函数名
        info = "函数[%s]的运行结果为%s" % (fun.__name__, result)
        log = "".join([now_time, " ", hostname, " ", process_name, " ", info])
        with open('file.log', 'a', encoding='utf-8') as f:
            f.write(log + '\n')
        return result

    return wrapper


@journal
def add(x, y):
    return x + y


@journal
def reduce(a, b):
    return a - b


reduce(7, 6)
add(4, 6)
