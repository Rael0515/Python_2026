def main() :
    n = 1
    print("구구단 프로그램 - 어떤 구구단을 원하십니까?")
    while(n):
        print("1. 2~9단 구구단")
        print("2. 특정 수 구구단")
        while(True):
        
            num = int(input("원하는 메뉴를 고르세요: "))
            if(num == 1):
                any_multi()
                break
            elif(num == 2):
                dan = int(input("원하는 구구단을 적으세요: "))
                multiplication(dan)
                break
            else:
                print("잘못입력했습니다. 다시 입력해주세요")
        while(True):
            yn = (input("프로그램을 종료하시겠습니까?(y or n): "))
            if(yn == 'y' or yn == 'Y'):
                break
            elif(yn == 'n' or yn =='N'):
                print("프로그램을 종료합니다")
                n = 0
                break

def any_multi():
    for i in range(2, 10, 1):
        print("-------%d단 -------" %(i))
        for j in range(1, 10, 1):
            print("%d * %d = %d" %(i, j, i*j))

def multiplication(dan):
    for j in range(1, 10, 1):
        print("%d * %d = %d" %(dan, j, dan*j))

main()