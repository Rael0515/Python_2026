### FILE: unit2.py

def processList(nlist):
    nlist.sort()
    return nlist

#print("unit2: ", __name__)

if __name__ == "__main__":
    list = [1,100,50,3]
    print(processList(list))