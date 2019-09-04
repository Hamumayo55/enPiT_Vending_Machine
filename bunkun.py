#お金が入っているか判定する関数
def insert():
    money = int(input("お金を入れてください: "))
    if money >= 300:
        return payment(True)
    else :
        return payment(False)

#商品が買えるか判定する関数
def payment(judge):
    if judge == True:
        return dispense("シャーペン")
    else :
        return dispense("ダミー")

#商品を排出する関数
def dispense(item):
    if item == "シャーペン":
        print("商品：シャーペン")
    else:
        print("お金が足りないよ")

def main():
    insert()

if __name__ == "__main__":
    main()


