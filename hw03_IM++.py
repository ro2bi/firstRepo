#Задача 1.
#Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 10.
#Користувач намагається вгадати число.
#Програма може давати підказки тільки "More", "Less", "You won!"
import math
import random

povt = True

while povt == True:
    rndm = random.randint(1, 10)
    print("Вгадайте загадане число у проміжку від 1 до 10!")
    vvod = int(input("Число: "))

    while vvod != rndm:
        if vvod < rndm:
            print("Більше!")
        elif vvod > rndm:
            print("Менше!")
        vvod = int(input("Спробуйте ще раз: "))

    print("Молодець! Ти вгадав загадане число!")
    print("Спробуй зіграти ще раз, або ")
    print("1) Набери Exit для виходу, та початку наступного завдання")
    print("2) Набери Again для повторної гри")
    vvod = input("Відповідь: ")

    if vvod.lower() == "exit":
        print("Дякую за гру!")
        povt = False
    elif vvod.lower() == "again":
        povt = True
    else:
        print("Некоректний ввід. Будь ласка, введіть 'Exit' або 'Again'.")
        vvod = input("Відповідь: ")
        while vvod.lower() != "exit" or vvod.lower() != "again":
            if vvod.lower() == "exit":
                print("Дякую за гру!")
                povt = False
                break
            elif vvod.lower() == "again":
                povt = True
                break
            else:
                print("Некоректний ввід. Будь ласка, введіть 'Exit' або 'Again'.")
                vvod = input("Відповідь: ")

######################################################################################

#Задача 2.
#Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 12.
#Програма виводить на екран число, яке створено і назву місяця, який відповідає цьому числу.

print ("")
print ("Друга задача")
print ("")

rndm = random.randint(1, 12)
mnth = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
print (rndm, "-", mnth[rndm-1])

##########################################################################################
#Задача 3.
#Написати програму в якій користувач вводить два цілих числа.
#Програма виводить результат піднесення першого числа у степінь відповідний другому числу.
#Зробити обробку всіх можливих помилок.
#В разі неможливості виконання дії - вивести відповідне повідомлення. ("Введено не число", тощо ... )

print ("")
print ("Третя задача")
print ("")

povt = True

while povt == True:
    try:
        integer = 0;
        num1 = int(input("Перше число: "))
        num2 = int(input("Друге число: "))

        if type(num1) == type(integer) and type(num2) == type(integer):
            res = math.pow(num1, num2)
            print(num1, "у степені", num2, " = ", res)
            povt = False

    except ValueError:
        print("Ви ввели не число.")
    except ZeroDivisionError:
        print("Перше число не може бути 0 якщо друге - негативне.")
