# code to simulate usage of an ATM machine

# names of me and my siblings in the ATM database
database = {"Kevan": 1000.0, "Kayleigh": 500.0, "Shane": 100.0}
names = ["Kevan", "Kayleigh", "Shane"]
transactions = ['D', 'W']
user = ""


# function to simulate the processes of the ATM
def useATM(name, transact, amt):
    if transact == 'D':
        database[name] = database[name] + amt
    elif transact == 'W':
        if database[name] - amt < 0:
            return False
        else:
            database[name] = database[name] - amt

    return True


# continues to prompt the user to make a transaction until they enter "end"
while user != "end":
    print(names)
    print("Please enter your name: ")
    user = input()

    # checks to make sure the name entered is in the database
    while not (user in names):
        print("That name is not in the database! Please enter a name in our system: ")
        user = input()

    print("Would you like to deposit or withdraw? Enter D or W:")
    dow = input()

    # checks to make sure the value entered is a valid process for the transaction (D or W)
    while not (dow in transactions):
        print("Please try again. Enter either D or W: ")
        dow = input()

    print("Please enter amount: ")
    amount = float(input())

    complete = useATM(user, dow, amount)
    # if the function returned True, the transaction was complete
    # if the function returned False, there were insufficient funds in the account
    if not complete:
        print("Insufficient funds.")
    print(database[user], " left in ", user, "'s account.")

    print("Would you like to make another transaction? Please enter Y or 'end': ")
    user = input()

print("ATM is shutting down...")
