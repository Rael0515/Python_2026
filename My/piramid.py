def piramid(num):
    for i in range(0, num):
        for j in range(0, num - i):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        for j in range(0, num - i):
            print(" ", end="")
        print("")

def main():
    again = 1
    while(again):
        num = int(input("원하시는 숫자를 입력하세요: "))
        piramid(num)
        while(1):
            yon = input("다시 하시겠습니까?(y or n): ")
            if((yon == 'n') or (yon == 'N')):
                again = 0
                break
            elif((yon == 'y') or (yon == 'Y')):
                break
            else:
                print("올바르지 않은 입력입니다. 다시 입력해주세요.")


main()