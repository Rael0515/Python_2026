import random
print("1부터 100까지의 숫자를 맞추는 게임입니다.")

num = random.randint(1,100)
count = 0
while True:
    guess = int(input("숫자를 입력하세요: "))
    count += 1
    if guess > num:
        print("숫자가 큽니다")
    elif guess < num:
        print("숫자가 작습니다")
    else:
        print("정답입니다.")
        break
print("총", count, "번 시도했습니다.")