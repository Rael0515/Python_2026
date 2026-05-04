from Enemy import *
from GetValue import *
from random import randint

def PlayerMove(player, enemy, turn):
    while True:
        print(turn, "턴|| 1. 공격 |2. 아이템사용|3. 도망(구현안함)")
        num = GetNumber(1, 3)
        if num == 1:
            print(player.name, "의 공격!")
            enemy.GetAttacked(player.DoAttack())
            turn += 1
            return turn
        elif num == 2:
            while True:
                print("1. 회복아이템 | 2. 공격아이템")
                item_num = GetNumber(1, 2)
                if item_num == 1: #회복아이템 이용
                    if player.ShowHealItem() == -1:
                        break
                    end = len(player.healItem)
                    print(end+1, ": 뒤로가기")
                    use_num = GetNumber(1, end+1)
                    if use_num == end+1:
                        break
                    else:
                        player.UseHealItem(use_num)
                        turn+=1
                        return turn
                elif item_num == 2: #공격아이템 이용
                    if player.ShowAttackItem() == -1:
                        break
                    end = len(player.attackItem)
                    print(end+1, ": 뒤로가기")
                    use_num = GetNumber(1, end+1)
                    if use_num == end+1:
                        break
                    else:
                        enemy.GetAttacked(player.UseAttackItem(use_num))
                        turn+=1
                        return turn
        else:
            print("System: 아직 구현되지 않은 행동입니다. 다른 행동을 선택해주세요.")
            

def EnemyMove(player, enemy):
    move_num = randint(1, 100)
    if move_num > 20:
        player.GetAttacked(enemy.DoAttacked())
        return 0
    else:
        enemy.DoNothing()
        return 0