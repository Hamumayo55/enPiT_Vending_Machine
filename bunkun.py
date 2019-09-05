import random
def insert(dict,dict_zai):
    #お金が入っているか判定する関数
    global MEMORYMONEY
    print("商品番号　　　　商品名　 　　　　　価格")
    for key,value in dict.items():
        product=value[0]
        price=value[1]
        print(key.center(8," "),end="")
        print(product.center(20," "),end="")
        print(str(price).center(10," "))
    #print()
    
    print(str("-"*40))
    select_number = input("買いたい商品の商品番号を選択してください: ")

    if dict_zai[dict[select_number][0]] <= 0:
        print("在庫がありません")
        return "dummy"
    
    try:
        money = int(input(str(dict[select_number][1])+"yen入れてください: "))
    except ValueError:
        money = 0

    MEMORYMONEY += money

    return dict[select_number][0]


def dispense(item, dict):
    #商品を排出する関数
    global MEMORYMONEY
    for value in dict.values():
        if item == value[0]:
            item_list=value

    if MEMORYMONEY<item_list[1]:
        diff_money = item_list[1] - MEMORYMONEY
        print(str(diff_money)+"yenのお金が足りないよ")

    else:
        check_purchase = input(item_list[0]+"を購入しますか(Yes/No): ")

            
        while True:
            if check_purchase == "Yes":
                MEMORYMONEY -= item_list[1]
                print("💖"*20)
                print("商品："+item_list[0])
                print("お釣りは"+str(MEMORYMONEY)+"yenです")
                i = random.randint(1,3)
                if i == 1:
                    print('今日も一日いいことがありますように')
                print('お買い上げありがとうございました')
                print("💖"*20)
                break

            elif check_purchase == "No":
                print("✋"*20)
                print("お釣りは"+str(MEMORYMONEY)+"yenです")
                print("ご利用ありがとうございました")
                print("✋"*20)
                break

            else:
                check_purchase = input("Yes/Noで入力してください(Yes/No)：")
        MEMORYMONEY = 0
        return item_list

    # else:
    #     diff_money = value[1] - MEMORYMONEY
    #     #item_count = counter(False,item)
    #     print(str(diff_money)+"yenのお金が足りないよ")
    #     #print("売り上げは"+str(item_count)+"yenです")

def counter(item_list, dict_uri,dict_zai):
    #商品をカウントする関数
    sum_uri = 0

    print(str("-"*20+"管理者モード"+"-"*20))
    for key,value in dict_uri.items():
        if key == item_list[0]:
            dict_uri[key] += item_list[1]
            dict_zai[key] -= 1
            print(key + "の売り上げは"+str(dict_uri[key])+"yenです")
        sum_uri += dict_uri[key]
        print(str(key)+":"+str(dict_zai[key])+"個")
    print("全体の売り上げは" + str(sum_uri) + "yenです")
            
    
def main():
    dict_bunkun={"1":["シャーペン",300], "2":["消しゴム",100],"3":["ルーズリーフ",150],"4":["シャー芯",200],"5":["シャー消しセット",500]}
    dict_uri = {"シャーペン":0, "消しゴム":0, "ルーズリーフ":0, "シャー芯":0,"シャー消しセット":0}
    dict_zai = {"シャーペン":100, "消しゴム":10, "ルーズリーフ":0, "シャー芯":0,"シャー消しセット":0}

    global MEMORYMONEY
    while True:
        print(str("*"*40))
        print('現在の投入金額は次の通りです:'+str(MEMORYMONEY)+"yenです")
        item = insert(dict_bunkun,dict_zai)
        if item != "dummy":
            item_list = dispense(item, dict_bunkun)
            if item_list != None:
                counter(item_list, dict_uri,dict_zai)
        


if __name__ == "__main__":
    MEMORYMONEY = 0
    main()
