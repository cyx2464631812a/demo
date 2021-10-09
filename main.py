'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：猜3次就睡眠 time.sleep(10)
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
import time
randint = random.randint(1, 30)  # 随机产生的数字
K = 0
while True:
    print(randint)
    K = K + 1
    num=input("请输入一个数字")
    if num.isdigit():
        num=int(num)
        if num == randint and K <= 3:
            print("OK")
            break
        elif num >randint and K < 3:
            print("猜大了")
        elif num <randint and K < 3:
            print("猜小了")
        else:
            time.sleep(10)
            break
    else:
        print("别瞎输入")
