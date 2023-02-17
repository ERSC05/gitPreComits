import random
import os
import time

numberTheUserWillSave = [0,0,0,0,0]
randomBoolNoOneCares = False

# [0] = how many 1 the user got and will save in the points
# [1] = how many 2 the user got and will save in the points
# [2] = how many 3 the user got and will save in the points
# [3] = how many 4 the user got and will save in the points
# [5] = how many 5 the user got and will save in the points
# [6] = how many 6 the user got and will save in the points
# ...
points = ["X","X","X","X","X","X","X","X","X","X","X","X","X"]
userKniffelCards = []
itemsTheUserWillKeep = [0,0,0,0,0]
indexOfItem = 0



def KI():
    return None
def KIStartPlay():

    return None
    # donerolls = DiceRoll()
    # singleDiceRow = diceToSavedNumber(donerolls,numberTheUserWillSave,itemsTheUserWillKeep)   

    # diceSaver(donerolls, i,numberTheUserWillSave,itemsTheUserWillKeep)

    
    return None
class KniffelCard:
    def __init__(self,howManyOne,howManyTwo,howManyThree,howManyFour,howManyFive,howManySix,countTripplePash,countFourPash,countFullHouse,countSmallStreet,countBigStreet,countKniffel,countChance):
        self.howManyOne = howManyOne
        self.howManyTwo = howManyTwo
        self.howManyThree = howManyThree
        self.howManyFour = howManyFour
        self.howManyFive = howManyFive
        self.howManySix = howManySix
        self.countTripplePash = countTripplePash
        self.countFourPash = countFourPash
        self.countFullHouse = countFullHouse
        self.countSmallStreet = countSmallStreet
        self.countBigStreet = countBigStreet
        self.countKniffel = countKniffel
        self.countChance = countChance

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')
#Returns the total sum of a list. If the list contains a string, only an arbitrary integer is returned as value
def SumIntegers(lst):
    total = 0
    for element in lst:
        if isinstance(element, int):
            total += element
    return total
def CheckBonusUpperArea(kniffelCardNrOne:KniffelCard):
#region List to add for the scoreboard
    listWithCardInfo = []
    listWithCardInfo.append(kniffelCardNrOne.howManyOne)
    listWithCardInfo.append(kniffelCardNrOne.howManyTwo)
    listWithCardInfo.append(kniffelCardNrOne.howManyThree)
    listWithCardInfo.append(kniffelCardNrOne.howManyFour)
    listWithCardInfo.append(kniffelCardNrOne.howManyFive)
    listWithCardInfo.append(kniffelCardNrOne.howManySix)
    # listWithCardInfo.append(kniffelCardNrOne.countTripplePash)
    # listWithCardInfo.append(kniffelCardNrOne.countFourPash)
    # listWithCardInfo.append(kniffelCardNrOne.countFullHouse)
    # listWithCardInfo.append(kniffelCardNrOne.countSmallStreet)
    # listWithCardInfo.append(kniffelCardNrOne.countBigStreet)
    # listWithCardInfo.append(kniffelCardNrOne.countKniffel)
    # listWithCardInfo.append(kniffelCardNrOne.countChance)
    #endregion    
    if SumIntegers(listWithCardInfo[0:5]) >= 63: 
        return 35
    else:
        return 0   
#Printing the Scoreboard at the 
def PrintPoins(kniffelCardNrOne:KniffelCard):
    clear_output()
    #region List to add for the scoreboard
    listWithCardInfo = []
    listWithCardInfo.append(kniffelCardNrOne.howManyOne)
    listWithCardInfo.append(kniffelCardNrOne.howManyTwo)
    listWithCardInfo.append(kniffelCardNrOne.howManyThree)
    listWithCardInfo.append(kniffelCardNrOne.howManyFour)
    listWithCardInfo.append(kniffelCardNrOne.howManyFive)
    listWithCardInfo.append(kniffelCardNrOne.howManySix)
    listWithCardInfo.append(kniffelCardNrOne.countTripplePash)
    listWithCardInfo.append(kniffelCardNrOne.countFourPash)
    listWithCardInfo.append(kniffelCardNrOne.countFullHouse)
    listWithCardInfo.append(kniffelCardNrOne.countSmallStreet)
    listWithCardInfo.append(kniffelCardNrOne.countBigStreet)
    listWithCardInfo.append(kniffelCardNrOne.countKniffel)
    listWithCardInfo.append(kniffelCardNrOne.countChance)
    #endregion
    print(f"""

1: count only one: {listWithCardInfo[0]}
2: count only two: {listWithCardInfo[1]}
3: count only three: {listWithCardInfo[2]}
4: count only four: {listWithCardInfo[3]}
5: count only five: {listWithCardInfo[4]}
6: count only six: {listWithCardInfo[5]}
----------------------------------------
            bonus: {CheckBonusUpperArea(kniffelCardNrOne)} 
entire upper area: {SumIntegers(listWithCardInfo)}

7: count Tripple Pash: {listWithCardInfo[6]}
8: count Four Pash: {listWithCardInfo[7]}
9: count Full House: {listWithCardInfo[8]}
10: count small Street: {listWithCardInfo[9]}
11: count big Street: {listWithCardInfo[10]}
12: count Kniffel: {listWithCardInfo[11]}
13: count Chance: {listWithCardInfo[12]}
-----------------------------------------
entire lower area: {SumIntegers(listWithCardInfo)}



""")
#Check how many singel dice exist
def CheckHowOftenExist(givenWorth,donerolls):
    summary = 0
    for number in donerolls:
        if number == givenWorth:
            summary= summary+number
    return summary
#Shows how the dice looks like
def PrintDice(rolls):
    dice = ["","","","","","",""]
    for i in rolls:
        diceNumber = []
        match(i):
            case 1:
                diceNumber.append("┌─────────┐")
                diceNumber.append("│         │")
                diceNumber.append("│    ●    │")
                diceNumber.append("│         │")
                diceNumber.append("└─────────┘")
            case 2:
                diceNumber.append("┌─────────┐")
                diceNumber.append("│  ●      │")
                diceNumber.append("│         │")
                diceNumber.append("│      ●  │")
                diceNumber.append("└─────────┘")
            case 3:
                diceNumber.append("┌─────────┐")
                diceNumber.append("│  ●      │")
                diceNumber.append("│    ●    │")
                diceNumber.append("│      ●  │")
                diceNumber.append("└─────────┘")
            case 4:
                diceNumber.append("┌─────────┐")
                diceNumber.append("│  ●   ●  │")
                diceNumber.append("|         |")
                diceNumber.append("│  ●   ●  │")
                diceNumber.append("└─────────┘")
            case 5:
                diceNumber.append("┌─────────┐")
                diceNumber.append("│  ●   ●  │")
                diceNumber.append("│    ●    │")
                diceNumber.append("│  ●   ●  │")
                diceNumber.append("└─────────┘")
            case 6:
                diceNumber.append("┌─────────┐")
                diceNumber.append("│  ●   ●  │")
                diceNumber.append("│  ●   ●  │")
                diceNumber.append("│  ●   ●  │")
                diceNumber.append("└─────────┘")
        dice[0] += diceNumber[0] + "   "
        dice[1] += diceNumber[1] + "   "
        dice[2] += diceNumber[2] + "   "
        dice[3] += diceNumber[3] + "   "
        dice[4] += diceNumber[4] + "   "
    return dice
#Return the dice values
def DiceRoll(): 
    #fill the List with random dice
    return [random.randint(1, 6) for i in range(5)]
#Check for 3 and 2 same dices
def FullHousCheck(donerolls):
    counts = [donerolls.count(i) for i in range(1, 7)]
    return 25 if 2 in counts and 3 in counts else 0
#Sum all numbers
def ChanceCheck(donerolls):
    return sum(donerolls)
#Ckechs if every dice got the same number
def KniffelCheck(donerolls):
    return 50 if donerolls[0] == donerolls[4] else 0
#Check if small (4) or big (5) street
def StreetCheck(big, donerolls):
    counterForList = 0
    counterForStreetLenth = 0
    donerolls.sort()
    for dice in donerolls:
        try:
            if len(donerolls) <= counterForStreetLenth or counterForList >= 5:
                break
        except:
            if dice == donerolls[counterForList+1]-1:
                counterForStreetLenth += 1
        if counterForList >= 4:
            counterForList -=1
        if dice == donerolls[counterForList+1]-1:
                counterForStreetLenth += 1
        counterForList +=1

    if counterForStreetLenth >=4 and big:
        return 40
    
    elif counterForStreetLenth >=3 and not big:
        return 25
    else:
        return 0
#Check if a Pash does exist
def PashCheck(worth,donerolls):
    which_number = int(input("Which number you want to save? "))
    count = donerolls.count(which_number)
    return sum(donerolls) if count >= worth - 4 else 0
#Manage the points (Where the User will safe the values)
def PointSystem(kniffelCardNrOne:KniffelCard, donerolls):
    while True:
        if not isinstance(kniffelCardNrOne,(int)):
            x = input("Wo willst du es hinspeichern")
            try:
                x = int(x)
            except:
                print(f"your input '({x})' is not a number")
                time.sleep(5)
            match(x):
                case 1:
                    if kniffelCardNrOne.howManyOne == "X":
                        kniffelCardNrOne.howManyOne = CheckHowOftenExist(x,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 2:
                    if kniffelCardNrOne.howManyTwo == "X":
                        kniffelCardNrOne.howManyTwo = CheckHowOftenExist(x,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 3:
                    if kniffelCardNrOne.howManyThree == "X":
                        kniffelCardNrOne.howManyThree = CheckHowOftenExist(x,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 4:
                    if kniffelCardNrOne.howManyFour == "X":
                        kniffelCardNrOne.howManyFour = CheckHowOftenExist(x,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 5:
                    if kniffelCardNrOne.howManyFive == "X":
                        kniffelCardNrOne.howManyFive = CheckHowOftenExist(x,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 6:
                    if  kniffelCardNrOne.howManySix == "X":
                        kniffelCardNrOne.howManySix = CheckHowOftenExist(x,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 7:
                    if kniffelCardNrOne.countTripplePash == "X":
                        kniffelCardNrOne.countTripplePash = PashCheck(x,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 8:
                    if kniffelCardNrOne.countFourPash == "X":
                        kniffelCardNrOne.countFourPash= PashCheck(x,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 9:
                    if kniffelCardNrOne.countFullHouse == "X":
                        kniffelCardNrOne.countFullHouse = FullHousCheck(donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 10:
                    if kniffelCardNrOne.countSmallStreet == "X":
                        kniffelCardNrOne.countSmallStreet = StreetCheck(False,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 11:
                    if kniffelCardNrOne.countBigStreet == "X":
                        kniffelCardNrOne.countBigStreet = StreetCheck(True,donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 12:
                    if kniffelCardNrOne.countKniffel == "X":
                        kniffelCardNrOne.countKniffel = KniffelCheck(donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case 13:
                    if kniffelCardNrOne.countChance == "X":
                        kniffelCardNrOne.countChance = ChanceCheck(donerolls)
                        break
                    else:
                        print("There are allready points.")
                        time.sleep(3)
                        continue
                case _:
                    print("your input was empty or not in range.")
                    print("You now return to rolling the dice.")
                    time.sleep(3)
                    continue
        else:
            print(f"Deine Punktzahl ist {sum(points)}.")
            input("Drücke um weiter zu spielen")
            break         
def diceSaver(donerolls, i,numberTheUserWillSave,itemsTheUserWillKeep):
    try:
        savedDice = input("Wilst du einen Würfel behalten? (1, 2, 3, 4, 5 oder 'N')")
        for dice in savedDice.split(" "):
            #merkt sich was gespeichert werden soll
            itemsTheUserWillKeep[int(dice)-1] = donerolls[int(dice)-1]
            indexOfItem = 0
            for keptItems in itemsTheUserWillKeep:
                match keptItems:
                    case 1:
                        numberTheUserWillSave[int(indexOfItem)] = donerolls[int(indexOfItem)]
                        indexOfItem+=1
                    case 2:
                        numberTheUserWillSave[int(indexOfItem)] = donerolls[int(indexOfItem)]
                        indexOfItem+=1
                    case 3:
                        numberTheUserWillSave[int(indexOfItem)] = donerolls[int(indexOfItem)]
                        indexOfItem+=1
                    case 4:
                        numberTheUserWillSave[int(indexOfItem)] = donerolls[int(indexOfItem)]
                        indexOfItem+=1
                    case 5:
                        numberTheUserWillSave[int(indexOfItem)] = donerolls[int(indexOfItem)]
                        indexOfItem+=1
                    case 6: 
                        numberTheUserWillSave[int(indexOfItem)] = donerolls[int(indexOfItem)]
                        indexOfItem+=1
                        continue
                    case 0:
                        indexOfItem+=1
                        continue
                    case _:
                        indexOfItem+=1
                        continue
    except:
        i +=1
def diceToSavedNumber(donerolls,numberTheUserWillSave,itemsTheUserWillKeep):
    indexOfItem = 0
    for saved in numberTheUserWillSave:
        if saved != int(0):
            donerolls[indexOfItem] = saved
            numberTheUserWillSave[indexOfItem] = 0
            itemsTheUserWillKeep[indexOfItem] = 0
        indexOfItem = indexOfItem+1
    singleDiceRow = PrintDice(donerolls)
    return singleDiceRow            
def GameStart():
    KIPlaying:bool = False
    amountOfPlayers = int(input("wie viele spiele wollen spielen oder Computer (999)"))
    if amountOfPlayers == 999:
        KI()
        amountOfPlayers = 2
        KIPlaying = True
    
    playerCounter = 0
    savedDice = 1
    rounds = 1
    kniffelCard = KniffelCard("X","X","X","X","X","X","X","X","X","X","X","X","X")
    kniffelCardList = []
    for x in range(amountOfPlayers):
        kniffelCardList.append(KniffelCard("X","X","X","X","X","X","X","X","X","X","X","X","X"))
    while rounds <= 5:
        print(f"Du bist in Runde: {rounds}")
        donerolls = []
        numberTheUserWillSave = [0,0,0,0,0]
        itemsTheUserWillKeep = [0,0,0,0,0]
        i = 1
        while i <= 3:
            clear_output()
            donerolls = DiceRoll()
            singleDiceRow = diceToSavedNumber(donerolls,numberTheUserWillSave,itemsTheUserWillKeep)   
            print(f"Player {playerCounter+1} is rolling...")
            print(singleDiceRow[0])
            print(singleDiceRow[1])
            print(singleDiceRow[2])
            print(singleDiceRow[3])
            print(singleDiceRow[4])         
            diceSaver(donerolls, i,numberTheUserWillSave,itemsTheUserWillKeep)
            i +=1
        
        PrintPoins(kniffelCard)
        PointSystem(kniffelCard, donerolls)
        donerolls = DiceRoll()

        if playerCounter == len(kniffelCardList) - 1:
            kniffelCardList[playerCounter] = kniffelCard
            playerCounter = 0
            rounds+=1
            kniffelCard = kniffelCardList[playerCounter] 
        else:
            kniffelCardList[playerCounter] = kniffelCard
            playerCounter += 1
            kniffelCard = kniffelCardList[playerCounter]
            if KIPlaying:
                KIStartPlay()




GameStart()



    