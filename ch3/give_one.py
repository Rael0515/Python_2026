print("구입액을 입력하시오.")
buy = int(input("구입액(단위: 만원): "))
if buy < 100:
    print(100 - buy, "만원만큼 더 구입하시면 사은품을 받을 수 있습니다.")
else:
    print("사은품을 받으실 수 있습니다.")