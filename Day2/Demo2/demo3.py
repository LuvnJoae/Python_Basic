# TextProBarV1.py

import time

scale = 10
print("{:-^20}".format("执行开始"))
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = i * 10
    print("{:^3} %[{}->{}]".format(c, a, b))
    time.sleep(1)
print("{:-^20}".format("执行结束"))