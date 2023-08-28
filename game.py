import math
import random
ROWS= 3
COLS= 3
# Intializing a dict to define symbools with their weight 
SYMBOLS_COUNT={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
#Multiplying factors associated with each letter 
SYMBOLS_VALUES={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}


# To get the valid Deposit amount, entered by the user
def deposit():
    while True:
        depositAmount=input("Enter a deposit amount: ")
        try:
            validDepositAmount=float(depositAmount)
        except ValueError:
            validDepositAmount=math.nan
        if math.isnan(validDepositAmount) or validDepositAmount <=0:
            print("Invalid....! Try again  ")
        else:
            return validDepositAmount

#Function to obtain Number of Lines user want to bet on ..
def getNumberofLines():
    while True:
        numberOfLines=input("Enter number of lines to bet on: ")
        try:
            validNumberOfLines=int(numberOfLines)
        except ValueError:
            validNumberOfLines=math.nan
        if math.isnan(validNumberOfLines) or validNumberOfLines <=0 or validNumberOfLines >3:
            print("Invalid....! Try again  ")
        else:
            return validNumberOfLines

#Function to Collect the valid bet from the user
def collectBet(balance, numberOfLines):
    while True:
        betAmount=input("Enter the Bet Amount: ")
        try:
            validBetAmount=float(betAmount)
        except ValueError:
            validBetAmount=math.nan
        if math.isnan(validBetAmount) or validBetAmount <=0 or validBetAmount >balance/numberOfLines:
            print("Invalid....! Try again  ")
        else:
            return validBetAmount

#Function to Spin the Sloth Machine by using Symbools (mentioned globaly)
def spin():
     symbols=[]
     for symbol,count in SYMBOLS_COUNT.items():
         for i in range(count):
            symbols.append(symbol)
     reels=[]
     for i in range(COLS):
        reels.append([])
        reelSymbols=symbols[:]
        for j in range(ROWS):
            randomIndex=math.floor(random.random()*len(reelSymbols))
            slectedSymbol=reelSymbols[randomIndex]
            reels[i].append(slectedSymbol)
            del reelSymbols[randomIndex]

     return reels
    
 #Transposing the colomuns to rows to compare whether a user Won or not ...    
def transpo(reels):
    rows=[]
    for i in range(ROWS):
        rows.append([])
        for j in range(COLS):
            rows[i].append(reels[j][i])

    return rows

#Print the obtained rows in the form of Sloth Machine
def printRows(rows):
    for i in rows:
        rowString=""
        for j,symbol in enumerate(i):
            rowString +=symbol
            if(j!=len(rows)-1):
                rowString+=" | "

        print(rowString)

#Get the winnings of the user 
def getWinnings(rows,bet,lines): 
    winnings=0
    for row in range(lines):
        symbols=rows[row]
        allSame=True
        for symbol in symbols:
         if(symbol != symbols[0]):
            allSame=False
            break
    if allSame:
        winnings += bet*SYMBOLS_VALUES[symbols[0]]
         
    return winnings
    
def game():
    balance=deposit()
    while(True):
        print(f"Your balance-- {balance}")
        numberOfLines=getNumberofLines()
        betAmount=collectBet(balance,numberOfLines)
        balance-=betAmount*numberOfLines
        reels= spin()
        rows=transpo(reels)
        printRows(rows)
        winnings=getWinnings(rows,betAmount,numberOfLines)
        balance +=winnings
        print(f"You won..! {winnings}")
        if(balance <=0):
            print("Sorry,You ran out of money..!")
            break
        playAgain=input("Do you want to play again (Y/N)?  ")
        if(playAgain.lower()!="y"):
            break

    
game()  #Play the Game.... 


