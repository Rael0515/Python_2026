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
        self.attackItem = [] #[[name, count, power]]
        self.healItem = [] #[[name, count, power]]

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

    def GetHealItem(self, item_name, num, power): #no return
        is_get = 0, totalcount = 0
        for item in self.healItem:
            if item[0] == item_name:
                item[1]+=num
                totalcount = item[1]
                is_get = 1
                break

        if is_get == 0:
            self.healItem.append([item_name, num, power])
            is_get = 1

        if is_get == 1:
            print(item_name,"을", num,"개 획득했다!")
            print("현재 ", item_name,"은(는) ", totalcount,"개 입니다.")

    def GetAttackItem(self, item_name, num, power): #no return
        is_get = 0, totalcount = 0
        for item in self.attackItem:
            if item[0] == item_name:
                item[1]+=num
                totalcount = item[1]
                is_get = 1
                break

        if is_get == 0:
            self.attackItem.append([item_name, num, power])
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

##실제 동작들

    def GetAttacked(self, dam): #return 0 || return self.hp, total 
        total = dam - self.defen
        if total <= 0:
            return 0
        self.hp -= total
        return self.hp, total
    
    def DoWAttack(self): #return total
        total = self.atk + self.weaponDam
        return total
