matchsticks = 22

print("\n\nDo not enter Invalid Numbers.\nNumbers above 4 are invalid.")
print("\nIf you do so, the computer automatically wins.")

while matchsticks >= 1:
    print(f"Number of matchstick available right now is {matchsticks}")
    print("\nYour Turn....")
    print("\nPickup the matchstick(s)-- (1-4): ")
    user = int(input())

    if user > 4:
        print("Invalid Selection")
        break

    computer = 5 - user

    print("\nComputer's Turn...\n")
    print(f"Computer chooses: {computer}")

    matchsticks = matchsticks - user - computer

    if matchsticks == 1:
        break

matchsticks = matchsticks - 1

print("Computer Wins....")
