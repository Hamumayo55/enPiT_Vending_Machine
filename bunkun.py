def insert():
    #お金が入っているか判定する関数
    money = int(input("お金を入れてください: "))
    if money >= 300:
        return payment(True)
    else :
        return payment(False)

def payment(judge):
    #商品が買えるか判定する関数
    if judge == True:
        return dispense("シャーペン")
    else :
        return dispense("ダミー")

def dispense(item):
    #商品を排出する関数
    if item == "シャーペン":
        item_count = counter(True)
        print("商品：シャーペン")
        print("売り上げは"+str(item_count)+"yenです")
    else:
        item_count = counter(False)
        print("お金が足りないよ")
        print("売り上げは"+str(item_count)+"yenです")

def counter(cnt):
    #商品をカウントする関数
    global CNTITEM 
    if cnt:
        CNTITEM += 1
        sales = CNTITEM * 300
        return sales
    else:
        sales = CNTITEM * 300
        return sales
    

def main():
    while True:
        insert()


if __name__ == "__main__":
    CNTITEM = 0
    main()


