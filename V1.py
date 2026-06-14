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
