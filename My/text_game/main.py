from Intro import Intro
from MoveMode import *
from ChoseMode import ChoseMode

def main():

    num = ChoseMode()

    match num:
        case 1:
            score = TestMode(Intro())
        case 2:
            score = NormalMode(Intro())
        case 3:
            score = InfinityMode(Intro())
    print("최종점수: ", score)
    return 0
  

main()        