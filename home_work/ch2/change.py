##연습문제1번
money = int(input("교환할 돈은 얼마?: "))
print("500원짜리 ==>", money // 500, "개")
money = money % 500
print("100원짜리 ==>", money // 100, "개")
money = money % 100
print("50원짜리 ==>", money // 50, "개")
money = money % 50
print("10원짜리 ==>", money // 10, "개")
money = money % 10
print("바꾸지 못한 잔돈 ==>", money, "원")
