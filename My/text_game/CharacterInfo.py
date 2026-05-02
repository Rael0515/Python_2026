from Item import getAttackItemList, getHealItemList

class Character:
    def __init__(self, name): #캐릭 생성 기본값
        self.name = name
        self.level = 1
        self.exp = 0
        self.maxhp = 100 #최대 hp
        self.hp = 100 #현재 hp
        self.atk = 10
        self.defen = 5

        self.money = 1000
        self.weaponName = "청동검"
        self.weaponDam = 5
        self.attackItem = [] #[[name, description, count, power]]
        self.healItem = [] #[[name, description, count, power]]

##내부 동작들
    def GetEXP(self, exp): #no return
        self.exp += exp
        while (self.exp - 100) >= 0 :
            self.level += 1
            self.maxhp += 50
            self.atk += 10
            self.defen += 5
            self.exp -= 100
        #return self.level, self.exp, self.maxhp, self.atk, self.defen
        
    def ChangeWeapon(self, name, dam): #no return
        self.weaponName = name
        self.weaponDam = dam

    def GetHealItem(self, item_name, description, num, power): #no return ##수정요함!
        is_get = 0
        totalcount = 0
        for item in self.healItem:
            if item[0] == item_name:
                item[1]+=num
                totalcount = item[1]
                is_get = 1
                break

        if is_get == 0:
            self.healItem.append([item_name, description, num, power])
            is_get = 1

        if is_get == 1:
            print(item_name,"을", num,"개 획득했다!")
            print("현재 ", item_name,"은(는) ", totalcount,"개 입니다.")

    def GetAttackItem(self, item_name, description, num, power): #no return
        is_get = 0
        totalcount = 0
        for item in self.attackItem:
            if item[0] == item_name:
                item[1]+=num
                totalcount = item[1]
                is_get = 1
                break

        if is_get == 0:
            self.attackItem.append([item_name, description, num, power])
            is_get = 1

        if is_get == 1:
            print(item_name,"을", num,"개 획득했다!")
            print("현재 ", item_name,"은(는) ", totalcount,"개 입니다.")

    def UseHealItem(self, item_name): #return 0 || return -1 (noItem)
        power = 0
        for item in self.healItem:
            if item[0] == item_name:
                item[1] -= 1
                power = item[2]
                self.hp += power
                if self.hp > self.maxhp:
                    self.hp = self.maxhp
                
                print(item[0], "을 사용했다!")
                print(self.name, "은(는) ",item[2],"만큼 회복했다!")

                if item[1] <= 0:
                    self.healItem.remove(item)
                    print("마지막 ", item[0], "을(를) 사용했다!")
                    return 0
                print("현재 ", item[0],"은 ", item[1], "개 남았다.")
                return 0
        return -1
    def UseAttackItem(self, item_name): #return power || return -1 (noItem)
        power = 0
        for item in self.attackItem:
            if item[0] == item_name:
                item[1] -= 1
                power = item[2]
                print(item[0], "을 사용했다!")

                if item[1] <= 0:
                    self.attackItem.remove(item)
                    print("마지막 ", item[0], "을(를) 사용했다!")
                    return power
                print("현재 ", item[0],"은 ", item[1], "개 남았다.")
                return power
        return -1

##기초치 획득
    def GetRecover(self, recover = 0, percent = 0): #return int(self.hp)
        if recover == 0:
            recover = int(self.maxhp * percent / 100)
        self.hp += recover
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return int(self.hp)
    
    def GetMoney(self, earn = 0, percent= 0):#return int(self.money)
        if earn == 0:
            earn = int(self.money*(percent/100))
        self.money+=earn
        return int(self.money)
    
##실제 동작들

    def GetAttacked(self, dam): #return 0 (no damage) || return self.hp, total (get damage)
        total = dam - self.defen
        if total <= 0:
            return 0
        self.hp -= total
        if self.hp <= 0:
            self.hp = 0
        while self.hp == 0:
            if self.ShowHealItem() == -1:
                self.Died(self)
            else:
                num = int(input(">> "))
                if num > 0 and num < len(self.healItem)+1:
                    self.UseHealItem()
                else:
                    print("존재하지 않는 아이템입니다.")
                    print("다시 입력해주세요.")
        return self.hp, total
    
    def DoWAttack(self): #return total
        total = self.atk + self.weaponDam
        return total
    
    def Died(self): #exit(0)
        print("캐릭터의 체력이 0이 되었습니다.")
        print("게임을 종료합니다.")
        exit(0)

##아이템 리스트 확인

    def ShowHealItem(self): #return -1(err) || return 0(normal)
        if not self.healItem:
            print("회복 아이템이 없습니다.")
            return -1
        else:
            index = 1
            print("---------------------------------------------------")
            for item in self.healItem: #[[name, description, count, power]]
                print(index, ". ", item[0])
                print("설명: ", item[1])
                print("회복량: ", item[3])
                print("아이탬 개수: ", item[2])    
                index+=1
                print("---------------------------------------------------")
        return 0
    
    def ShowAttackItem(self): #return -1(err) || return 0(normal)
        if not self.attackItem:
            print("공격 아이템이 없습니다.")
            return -1
        else:
            index = 1
            print("---------------------------------------------------")
            for item in self.attackItem: #[[name, description, count, power]]
                print(index, ". ", item[0])
                print("설명: ", item[1])
                print("데미지: ", item[3])
                print("아이탬 개수: ", item[2])    
                index+=1
                print("---------------------------------------------------")
        return 0
