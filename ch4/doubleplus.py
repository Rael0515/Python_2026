num1 = int(input("*** 첫번째 숫자를 입력하세요 : "))
num2 = int(input("*** 두번째 숫자를 입력하세요 : "))
range1 = int(input("*** 더할 숫자를 입력하세요 : "))
sum = 0
for i in range(num1, num2+1,range1):
    sum += i
print(num1,"+",num1+range1,"+...+", num2, "는 ", sum,"입니다.")
