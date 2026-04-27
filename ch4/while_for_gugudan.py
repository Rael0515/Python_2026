i = 2
print("----------------------")
while i < 6:
    for j in range(1, 10, 1):
        print("%d x %d = %d" %(i,j,i*j))
    i+=1
    print("----------------------")