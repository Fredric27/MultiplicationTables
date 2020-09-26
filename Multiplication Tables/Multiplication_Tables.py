import random

a=1

while a==1:
    listNum = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    num1 = random.choice(listNum)
    num2 = random.choice(listNum)

    answer = input("Quanto fa " + num1 + "x" + num2 + "?\n")

    inum1 = int(num1)
    inum2 = int(num2)

    result = inum1 * inum2
    resultStr = str(result)

    if resultStr == answer:
        print("Bravo! Il risultato è corretto!\n")
    if resultStr != answer:
        print("No... " + num1 + " x " + num2 + " fa " + resultStr + "! \n")

