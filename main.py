coin = 0

drinkName = []
drinkPrice = []

def Init():
    AddDrink("빨간포션", 500)
    AddDrink("파란포션", 500)
    AddDrink("주황포션", 800)
    AddDrink("노란포션", 800)

def AddDrink(name, price):
    global drinkName, drinkPrice

    drinkName.append(name)
    drinkPrice.append(price)

def InsertCoin():
    return int(input())

def SelectDrink(name):
    global coin

    index = -1

    for i in range(0, len(drinkName)):
        if(name == drinkName[i]):
            index = i
            break


    if(drinkPrice[index] <= coin):
        coin -= drinkPrice[index]
        print(drinkName[index], "(을)를 구매했습니다.")
        print("거스름돈", coin, "원이 나왔습니다.")
    else:
        print("금액이 부족합니다")

    ShowMenu()

def ShowMenu():
    global coin
    print("현금을 투입해주세요")
    coin = InsertCoin()

    print(drinkName)
    print(drinkPrice)

    print("음료수를 선택해주세요")
    SelectDrink(input())

def Main():
    Init()

    print("환영합니다.")
    ShowMenu()

Main()