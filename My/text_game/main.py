from CharacterInfo import Character
from Intro import Intro
from MoveMode import *
from ChoseMode import ChoseMode

def main():

    Intro()

    match ChoseMode():
        case 1:
            TestMode()
        case 2:
            NormalMode()
        case 3:
            InfinityMode()
    
    return 0
  

main()        