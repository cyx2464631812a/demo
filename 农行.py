import random

print("***************************")
print("*    中国农业银行账户管理系统  *")
print("***************************")
print("*          1、开户         *")
print("*          2、存钱         *")
print("*          3、取钱         *")
print("*          4、转账         *")
print("*          5、查询         *")
print("*          6、再见         *")
print("***************************")
bank = {}
bank_name = "中国农业银行肇东分行"


def bank_add(account, username, password, country, province, street, door):
    if username in bank:
        return 2
    elif len(bank) >= 100:
        return 3

    else:
        bank[username] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        return 1



def useradd():
    account = random.randint(10000000, 99999999)
    username = input("请输入您的用户名")
    password = input("请输入您的用户密码")
    print("下面请输入你的详细地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    add = bank_add(account, username, password, country, province, street, door)
    if add == 3:
        print("数据库已满请到其他银行开户")
    elif add == 2:
        print("请输入其他用户名")
    elif add == 1:
        print("开户成功,下面是你的详细信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))


def savemoney():
    username = input("输入用户名")
    if username in bank:
        moneynum = input("请输入存款金额")
        bank[username]["money"] = moneynum


def getmoney():
    username = input("请输入用户名")
    if username in bank:
        password = input("请输入 ；密码")
        if password == bank[username][password]:
            getmoney = int(input("输入取款金额"))
            if getmoney > bank[username]['money']:
                print("error")
            elif getmoney <= bank[username]['money']:
                bank[username]['money'] = bank[username]['money'] - getmoney
            print("你的余额为：", bank[username]['money'])


def transferaccounts():
    username = input("请输入用户名")
    if username in bank:
        password = input("请输入密码")
        if password in bank:
            input("请输入转入账户用户名")
            getmoney = int(input("输入转账金额"))
            if getmoney > bank[username]['money']:
                print("error")
            elif getmoney <= bank[username]['money']:
                bank[username]['money'] = bank[username]['money'] - getmoney
            print("你的余额为：", bank[username]['money'])


def query():
    username = input("请输入用户名")
    if username in bank:
        password = input("请输入密码")
        if password in bank:
            print("你的余额为：", bank[username]['money'])


while True:
    index = int(input("请输入您的操作"))
    if index == 1:
        print("1、开户")
        useradd()
        print(bank)
    elif index == 2:
        print("2、存钱")
        savemoney()
    elif index == 3:
        print("3、取钱")
    elif index == 4:
        print("4、转账")
        transferaccounts()
    elif index == 5:
        print("5、查询")
        query()
    elif index == 6:
        print("感谢使用再见")
        break

