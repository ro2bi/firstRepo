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
        print("1) Набери Exit для виходу")
        print("2) Набери Again для повторної гри")
        vvod = input("Відповідь: ")

        if vvod.lower() == "exit":
            print("Дякую за гру!")
            povt = False
        elif vvod.lower() == "again":
            povt = True
        else:
            print("Некоректний ввід. Будь ласка, введіть 'Exit' або 'Again'.")