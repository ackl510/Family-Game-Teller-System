import random
import time

start = False
print("Welcome to the Bank Manager!")
time.sleep(0.5)

# --- Setup number of players ---
num_players = int(input("How many players? "))

# --- Setup starting money ---
starting_money = int(input("Starting money for each player? "))

# --- Create players dynamically ---
players = {}
for i in range(1, num_players + 1):
    players[f"Player_{i}"] = starting_money

print("Players created:", ", ".join(players.keys()))
time.sleep(2)
time.sleep(2)
print("This system is used to manage the money of players in a game")
time.sleep(2)
print("This system is used to charge players, give them money, transfer money between players, and declare bankruptcy for players")
time.sleep(2)
print("The commands are based on a /{command} system")
time.sleep(2)
print("Type /help for a list of commands")


print("Commands:")
print("/roll")
print("/charge")
print("/give")
print("/transfer")
print("/bankrupt")
print("/end")
start = True
# --- Main loop ---
while start:
    command = input("Enter Command: ")

    if command == "/charge":
        name = input("Who would you like to charge? ")
        amount = int(input("How much? "))
        players[name] -= amount
        print(name, "now has $", players[name])

    elif command == "/give":
        name = input("Who would you like to give money to? ")
        amount = int(input("How much? "))
        players[name] += amount
        print(name, "now has $", players[name])

    elif command == "/transfer":
        sender = input("Transfer FROM: ")
        receiver = input("Transfer TO: ")
        amount = int(input("How much? "))
        players[sender] -= amount
        players[receiver] += amount
        print(sender, "now has $", players[sender])
        print(receiver, "now has $", players[receiver])

    elif command == "/bankrupt":
        name = input("Who is bankrupt? ")
        players[name] = 0
        print(name, "now has $0")

    elif command == "/roll":
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print("You rolled", d1, "and", d2, "=", d1+d2)

        if d1 == d2:
            print("Doubles! Roll again!")

    elif command == "/help":
        print("Commands:")
        print("/roll")
        print("/charge")
        print("/give")
        print("/transfer")
        print("/bankrupt")
        print("/end")

    elif command == "/end":
        print("Final totals:")
