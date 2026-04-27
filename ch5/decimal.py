def main():
    print("이진수변환 >> " + decimal(int(input("원하는 양의 정수를 입력하시오: "))))

def decimal(x):
    result = ' '
    while(x > 0):
        remainder = x % 2
        x = x // 2
        result  = str(remainder) + result
    return result

main()