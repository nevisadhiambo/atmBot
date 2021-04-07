import secrets
import string
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #for email validation

database = {}


#services offered
def services():
    serviceSelected = int(input("Select: \n 1. Withdrawal\n 2. Deposit\n 3. Mini Statement/ AccountBalance\n 4. Sign out\n 5. exit\n"))
                                          
    if (serviceSelected == 1):
        withdrawal()
    elif(serviceSelected == 2):
        deposit()
    elif(serviceSelected == 3):
        miniStatement()
    elif(serviceSelected == 4):
        login()
    elif(serviceSelected == 5):
        exit()
    else:
        print(" Invalid choice. Try again")
    
#login
def login():
    print("Login to your account")
    print("= =" *8)


    #validate user
    def validateUserAccount():
        userAccount = input("Please enter your account Number \n")
        print("= =" *8)
        userPassword = input("Enter your password \n")
        print("= =" *8)
        for accNumber, userDetails in database.items():
            if(accNumber == userAccount):
                if(userDetails[4] == userPassword):
                    print("Login successful")
                    print("= =" *8)

                    #available services
                    print("These are the available services")
                    services()                        
            else:
                print("Username or password is wrong. Please try again")
                print("= = " *8)
                validateUserAccount()    
    validateUserAccount()


# register
def register():
    
    print("Create your account")
    print("= =" *8)

    fName = input("What's your first name? \n") 
    print("= =" *8)

    lName = input("What's your Last name? \n")
    print("= =" *8)
    
   #email validation
    def validateEmail():    
        email = input("What's your email address? \n")
        print("= =" *8)
        if(re.search(regex,email)):

            #Amount required to start an account 
            acountBalance = float(input("How much would you like to start your account with?\n"))
            print("= =" *8)

            pword = input("Create your password \n")
            print("= =" *8)


            confirmPword = input("confirm your password \n")
            print("= =" *8)

            #password validation
            if (confirmPword == pword):    

                #generate account number

                M = 10

                accNumber = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for i in range(M))               

                database[accNumber] = [fName, lName, email, acountBalance, pword]

                print("Welcome " + fName.capitalize() + " " + lName.capitalize() + " " + "to Family bank")
                
                print("Your account Number is " + str(accNumber))
                print("= =" *8)

                #print(database)
                login()
            else:
                 print("Password does not match. Try Again")
                 register()
        else:
            print("Invalid email. Try again")
            validateEmail()
    validateEmail()


#withdrawal
def withdrawal():
    amount = float(input("How much would you like to withdraw? \n"))
    for accNumber, userDetails in database.items():
         if(userDetails[3] >= amount):
             print("Take your cash")
             userDetails[3] -= amount
             print("You account Balance is $%d"  % userDetails[3])
             print("What would you like to do next? Select a service")
             services()
        
         else:
            print("Insufficient funds. Top up and Try again")
            print("You account Balance is $%d"  % userDetails[3])
            print("What would you like to do next? Select a service")
            services()

#deposit
def deposit():
    amount = float(input("How much would you like to deposit? \n"))
    for accNumber, userDetails in database.items():
        userDetails[3] += amount
        print("Your account Balance is $%d" % userDetails[3])
        print("What would you like to do next? Select a service")
        services()


#mini statement
def miniStatement():
    for accNumber, userDetails in database.items():
        print("You account balance is $%d" %userDetails[3])
        print("What would you like to do next? Select a service")
        services()


            
#initialize the program
def init():
    print("Welcome to Family Bank")
    print("= =" *8)

    print("You can always count on family")
    print("= =" *8)

    selectedOption = int(input("Select \n 1. To register \n 2. To Login \n"))

    if (selectedOption == 1):
        register()
        
    elif(selectedOption == 2):
        login()
        
    else:
        print("Invalid choice, try again")
        init()
    
init()

