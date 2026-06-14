import random

print("Welcome to the Bank Manager!")

# --- Setup number of players ---
num_players = int(input("How many players? "))

# --- Setup starting money ---
starting_money = int(input("Starting money for each player? "))

# --- Create players dynamically ---
players = {}
for i in range(1, num_players + 1):
    players["Player_" + str(i)] = starting_money

print("Players created:", ", ".join(players.keys()))
print("This system is used to manage the money of players in a game")
print("Type /help for a list of commands")

print("Commands:")
print("/roll")
print("/charge")
print("/give")
print("/transfer")
print("/bankrupt")
print("/end")

# --- Main loop ---
while True:
    command = input("Enter Command: ")

    # Charge a player
    if command == "/charge":
        name = input("Who would you like to charge? ")
        amount = int(input("How much? "))
        players[name] -= amount
        print(name + " now has $" + str(players[name]))

    # Give money to a player
    elif command == "/give":
        name = input("Who would you like to give money to? ")
        amount = int(input("How much? "))
        players[name] += amount
        print(name + " now has $" + str(players[name]))

    # Transfer money between players
    elif command == "/transfer":
        sender = input("Transfer FROM: ")
        receiver = input("Transfer TO: ")
        amount = int(input("How much? "))
        players[sender] -= amount
        players[receiver] += amount
        print(sender + " now has $" + str(players[sender]))
        print(receiver + " now has $" + str(players[receiver]))

    # Declare bankruptcy
    elif command == "/bankrupt":
        name = input("Who is bankrupt? ")
        players[name] = 0
        print(name + " now has $0")

    # Roll dice
    elif command == "/roll":
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print("You rolled", d1, "and", d2, "=", d1 + d2)

        if d1 == d2:
            print("Doubles! Roll again!")

    # Help menu
    elif command == "/help":
        print("Commands:")
        print("/roll")
        print("/charge")
        print("/give")
        print("/transfer")
        print("/bankrupt")
        print("/end")

    # End game
    elif command == "/end":
        print("Final totals:")
        for name in players:
            print(name + " has $" + str(players[name]))
        break

    # Unknown command
    else:
        print("Unknown command. Type /help")
