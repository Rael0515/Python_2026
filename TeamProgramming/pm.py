### FILE: pm.py
from unit1 import *
from unit2 import *
from unit3 import *
def main():
    nlist = readList()
    processList(nlist)
    printList(nlist)
# print (“pm:”,__name__)
if __name__ == "__main__":
    main()