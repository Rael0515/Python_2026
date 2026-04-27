pro_love = "교수님사랑해"
str_len = len(pro_love)


for i in range(0, str_len):
    for j in range(i+1):
        print(pro_love[j], end="")
    print()

for i in range(str_len-2, -1, -1):
    for i in range(i+1):
        print(pro_love[j], end="")
    print()
    
