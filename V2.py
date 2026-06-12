import time
import sys
import random
Player_1=1500
Player_2=1500
Player_3=1500
Player_4=1500

Camount=0
while True:
    command=input("Enter Command")
    if command=="/charge":
        Cperson=input("Who would you like to charge?")
        charge=int(input("How much would you like to charge them?"))
        if Cperson=="Player_1":
            Player_1=Player_1-charge
            print("Player_1 has $",Player_1)
        if Cperson=="Player_2":
            Player_2=Player_2-charge
            print("Player_2 has $",Player_2)
        if Cperson=="Player_3":
            Player_3=Player_3-charge
            print("Player_3 has $",Player_3)
        if Cperson=="Player_4":
            Player_4=Player_4-charge
            print("Player_4 has $",Player_4)
    if command=="/give":
        Gperson=input("Who would you like to give money to?")
        give=int(input("How much would you like to give them?"))
        if Gperson=="Player_1":
            Player_1=Player_1+give
            print("Player_1 has $",Player_1)
        if Gperson=="Player_2":
            Player_2=Player_2+give
            print("Player_2 has $",Player_2)
        if Gperson=="Player_3":
            Player_3=Player_3+give
            print("Player_3 has $",Player_3)
        if Gperson=="Player_4":
            Player_4=Player_4+give
            print("Player_4 has $",Player_4)
    if command=="/transfer":
        Tperson1=input("Who would you like to transfer money from?")
        Tperson2=input("Who would you like to transfer money to?")
        transfer=int(input("How much would you like to transfer?"))
        if Tperson1=="Player_1":
            Player_1=Player_1-transfer
            print("Player_1 has $",Player_1)
        if Tperson1=="Player_2":
            Player_2=Player_2-transfer
            print("Player_2 has $",Player_2)
        if Tperson1=="Player_3":
            Player_3=Player_3-transfer
            print("Player_3 has $",Player_3)
        if Tperson1=="Player_4":
            Player_4=Player_4-transfer
            print("Player_4 has $",Player_4)
        if Tperson2=="Player_1":
            Player_1=Player_1+transfer
            print("Player_1 has $",Player_1)
        if Tperson2=="Player_2":
            Player_2=Player_2+transfer
            print("Player_2 has $",Player_2)
        if Tperson2=="Player_3":
            Player_3=Player_3+transfer
            print("Player_3 has $",Player_3)
        if Tperson2=="Player_4":
            Player_4=Player_4+transfer
            print("Player_4 has $",Player_4)
    if command == "/bankcrupt":
        Bperson=input("Who would you like to bankcrupt?")
        if Bperson=="Player_1":
            Player_1=0
            print("Player_1 has $",Player_1)
        if Bperson=="Player_2":
            Player_2=0
            print("Player_2 has $",Player_2)
        if Bperson=="Player_3":
            Player_3=0
            print("Player_3 has $",Player_3)
        if Bperson=="Player_4":
            Player_4=0
            print("Player_4 has $",Player_4)
    if command=="/roll":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print("You rolled a",dice1,"and a",dice2,"for a total of",dice1+dice2)
        if dice1==dice2:
            print("You rolled doubles! Roll again!")
            dice1=random.randint(1,6)
            dice2=random.randint(1,6)
            print("You rolled a",dice1,"and a",dice2,"for a total of",dice1+dice2)
            if dice1==dice2:
                print("You rolled doubles again! Roll again!")
                dice1=random.randint(1,6)
                dice2=random.randint(1,6)
                print("You rolled a",dice1,"and a",dice2,"for a total of",dice1+dice2)
                if dice1==dice2:
                    print("You rolled doubles three times in a row! You are now in jail!")
    if command=="/help":
        print(" Try one of the following:")
        print("/roll - Roll a dice")
        print("/charge - Charge a player money")
        print("/give - Give a player money")
        print("/transfer - Transfer money from one player to another")
        print("/bankcrupt - Bankcrupt a player")
        print("/help - Show this help message")
        print("/end - End the game and total everybodies score")
    if command!="/charge" and command!="/give" and command!="/transfer" and command!="/bankcrupt" and command!="/help" and command!="/end" and command!="/roll":
        print(" Try one of the following:")
        print("/roll - Roll a dice")
        print("/charge - Charge a player money")
        print("/give - Give a player money")
        print("/transfer - Transfer money from one player to another")
        print("/bankcrupt - Bankcrupt a player")
        print("/help - Show this help message")
        print("/end - End the game and total everybodies score")
    if command=="/end":
        print("Player_1 has $",Player_1)
        print("Player_2 has $",Player_2)
        print("Player_3 has $",Player_3)
        print("Player_4 has $",Player_4)
        break