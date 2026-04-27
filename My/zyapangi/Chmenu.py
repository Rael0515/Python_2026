def Chmenu(num, menu):
    print("당신은 %d번 %s를 구매하셨습니다." %(num, menu[num - 1][0]))

    return(int(menu[num - 1][1]))