

def insert(dict):
    #お金が入っているか判定する関数
    global MEMORYMONEY
    display=dict
    print(display)

    
    
    select_number = input("買いたい商品の商品番号を選択してください")

    try:
        money = int(input(str(display[select_number][1])+"yen入れてください: "))
    except ValueError:
        money = 0

    MEMORYMONEY += money

    # for key,value in display.items():
    #     if value[1] <= MEMORYMONEY:
    #         print(key,value)

    if MEMORYMONEY >= display[select_number][1]:
        return payment(True, display[select_number][0])
    else :
        return payment(False, display[select_number][0])

def payment(judge, item):
    #商品が買えるか判定する関数
    if judge == True:
        return dispense(item)
    else :
        return dispense("ダミー")

def dispense(item):
    #商品を排出する関数
    global MEMORYMONEY
    if item == "シャーペン":
        check_purchase = input(item+"を購入しますか(Yes/No): ")
        
        while True:
            if check_purchase == "Yes":
                MEMORYMONEY -= 300
                item_count = counter(True,item)
                print("商品："+item)
                print("お釣りは"+str(MEMORYMONEY)+"yenです")
                print("シャーペンの売り上げは"+str(item_count)+"yenです")
                break

            elif check_purchase == "No":
                print("お釣りは"+str(MEMORYMONEY)+"yenです")
                break

            else:
                check_purchase = input("Yes/Noで入力してください(Yes/No)：")
        MEMORYMONEY = 0
        
    elif item == "消しゴム":
        check_purchase = input(item+"を購入しますか(Yes/No): ")
        
        while True:
            if check_purchase == "Yes":
                MEMORYMONEY -= 200
                item_count = counter(True,item)
                print("商品："+item)
                print("お釣りは"+str(MEMORYMONEY)+"yenです")
                print("消しゴムの売り上げは"+str(item_count)+"yenです")
                break

            elif check_purchase == "No":
                print("お釣りは"+str(MEMORYMONEY)+"yenです")
                break

            else:
                check_purchase = input("Yes/Noで入力してください(Yes/No)：")
        MEMORYMONEY = 0

    else:
        diff_money = 300 - MEMORYMONEY
        item_count = counter(False,item)
        print(str(diff_money)+"yenのお金が足りないよ")
        #print("売り上げは"+str(item_count)+"yenです")

def counter(cnt,item):
    #商品をカウントする関数
    global CNTITEM_sy
    global CNTITEM_kesi
    if item == "シャーペン":
        if cnt:
            CNTITEM_sy += 1
            sales = CNTITEM_sy * 300
            return sales
        else:
            sales = CNTITEM_sy * 300
            return sales
    elif item == "消しゴム":
        if cnt:
            CNTITEM_kesi += 1
            sales = CNTITEM_kesi * 200
            return sales
        else:
            sales = CNTITEM_kesi * 200
            return sales
    else:
        return 

    
def main():
    dict_bunkun={"1":["シャーペン",300], "2":["消しゴム",200]}
    print(dict_bunkun["1"][0])
    global MEMORYMONEY
    while True:
        print(str("-"*40))
        print('現在の投入金額は次の通りです:'+str(MEMORYMONEY)+"yenです")
        insert(dict_bunkun)

if __name__ == "__main__":
    CNTITEM_sy = 0
    CNTITEM_kesi = 0
    MEMORYMONEY = 0
    main()
