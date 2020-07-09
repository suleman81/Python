users_ID = []
users_Email = []
users_PSW = []

def login():
    ID = input("Enter your Email or username: ")
    PSW = input("Enter your Password: ")
    if ID in users_Email or ID in users_ID:
        if PSW in users_PSW:
            print("Welcome to My program")
        else: 
            print("You Enter Wrong Password\n\nTry Again....")
            login()
    elif ID not in users_Email or users_ID:
        print("Sorry we did not find your account\n\n Do you want to signup or login again (S/L)")
        y = input()
        if y.lower() == "s":
            signup()
        elif y.lower() == "l":
            login()
        else:
            print("Nice to meet you user |  Good Bye")


def signup():
    username = input("Enter your username: ")
    Email = input("Enter your Email: ")
    PSW = input("Enter your Password: ")
    if username not in users_ID:
        users_ID.append(username)
    if Email not in users_Email:
        users_Email.append(Email)
    if PSW not in users_PSW:
        users_PSW.append(PSW)
    if username == users_ID:
        print("This user name is not Availlabe")
        signup()
    if Email == users_Email:
        print("Looks like you already have an account")
        signup()
    
    print(users_ID,users_Email,users_PSW,sep='\n')
    print("Your Account is created\n\n Do you want to login(Y/N): ")
    y = input()
    if y.lower() == "y":
        login()
    else:
        print("Nice to meet you new user |  Good Bye")


print("Select Your choice:\n 1: Login\n 2: Signup")

choice = int(input())

if choice == 1:
    login()
elif choice == 2:
    signup()
else:
    print("you enter wrong input")     