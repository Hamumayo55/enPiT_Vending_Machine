def insert():
    #お金が入っているか判定する関数
    global MEMORYMONEY
    try:
        money = int(input("お金を入れてください: "))
    except ValueError:
        money = 0

    MEMORYMONEY += money

    if MEMORYMONEY >= 300:
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
    global MEMORYMONEY
    if item == "シャーペン":
        check_purchase = input("シャーペンを購入しますか(Yes/No): ")
        while True:
            if check_purchase == "Yes":
                MEMORYMONEY -= 300
                item_count = counter(True)
                print("商品：シャーペン")
                print("お釣りは"+str(MEMORYMONEY)+"yenです")
                break

            elif check_purchase == "No":
                print("お釣りは"+str(MEMORYMONEY)+"yenです")
                break

            else:
                check_purchase = input("Yes/Noで入力してください(Yes/No)：")

        MEMORYMONEY = 0
        #print("売り上げは"+str(item_count)+"yenです")
    else:
        diff_money = 300 - MEMORYMONEY
        item_count = counter(False)
        print(str(diff_money)+"yenのお金が足りないよ")
        #print("売り上げは"+str(item_count)+"yenです")

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
    global MEMORYMONEY
    while True:
        print(str("-"*40))
        print('現在の投入金額は次の通りです:'+str(MEMORYMONEY)+"yenです")
        insert()

if __name__ == "__main__":
    CNTITEM = 0
    MEMORYMONEY = 0
    main()
