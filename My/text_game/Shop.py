from Item import *
from GetValue import *

def Shop(player):
    print("여기는 상점이란다. 무엇을 사러 왔니?")
    while num != 3:
        print("1. 회복아이템, 2. 공격아이템 3. 끝내기")
        num = GetNumber(1, 3)
        if num ==1:
            ShowHealItemList()
            shop_item = GetNumber(0, len(getHealItemList()))
            if shop_item != 0:
                BuyHealItem(player, shop_item)
            else:
                print("그래? 안살거니?")
            
        if num == 2:
            ShowAttackItemList()
            shop_item = GetNumber(0, len(getAttackItemList()))
            if shop_item != 0:
                BuyAttackItem(player, shop_item)
            else:
                print("그래? 안살거니?")
        else:
            print("또 오렴!")