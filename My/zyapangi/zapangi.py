from menuList import menuList 
from SeeList import SeeList
from Chmenu import Chmenu

def main():
    sum = 0
    while True:
        print("먹고 싶은 음식의 번호는?(끝내려면 0)")
        SeeList(menuList())
        num = int(input(">>"))
        if((num > 5) or (num < 0)):
            print("잘못된 번호를 선택하셨습니다.")
        elif(num == 0):
            break
        else:
            sum += Chmenu(num, menuList())

    print("최종 구매 금액은: %d" %(sum))
    print("종료합니다.")

main()