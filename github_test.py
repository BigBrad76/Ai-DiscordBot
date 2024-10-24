'''
Welcome to the Github Test!
I've written some code as well as put instructions below for each of you to specifically include.

THIS IS MEANT TO CHALLENGE YOUR ABILITY TO PROGRAM, YOU ARE EXPECTED TO NEED AND ASK FOR HELP.

Make sure you understand the following of this mini project:
    1.) What each persons segment of the code is meant to do, and how they did it.
    2.) What the overall code is supposed to accomplish.

You will be expected to do the following:
    1.) Write code in your section to accomplish your specific task, but keep variables and imports in the shared areas up top. (Replace the print statement in your function with the actual application of your code)
    2.) Upload the updated code into GitHub
    3.) Message Brad for approval when you have your code put in GitHub.
    4.) If you need to write your code in someone else's section, contact and collaborate with them!

If you have any questions, contact any of your teammates, remember that we are all a team together!
Not one of us is better than another, nor more important than another. Feel free to work with eachother on our combined code, even in individual sections.
Contribute what you can and it will be magnified to an equal portion regardless of initial ability

No matter what, don't dare to devalue your role in this team. If you apply what you can, you will grow exponentially.
'''

#Bank Account Manager Program Start:

#Imports:


#Variables:
selection = "" #This variable will be used to determine which of our modules to run.
main_menu = True #This variable will be used to maintain a loop in the main menu until the user selects one of our modules.

#Austin's Code: 
'''
Account Creation and Management

Objective: Write a module that allows users to create an account, set up a username and pin, then store that data.

Key Functions:
    1.) Create a new account by asking for a name, PIN, and initial deposit.
    2.) Store account data (name, PIN, balance) in a dictionary or list.
    3.) Allow the user to update account information (like changing a PIN).
'''
def create():
    print(f"Creating account...")

#Brad's Code:
'''
Deposit and Withdrawal System

Objective: Build a system where users can deposit or withdraw money from their accounts.

Key Functions:
    1.) Ask the user for their account information (name and PIN) to access their account.
    2.) Allow the user to deposit or withdraw money (update account balance).
    3.) Ensure withdrawal requests do not exceed the account balance (error handling using if statements).
'''
def deposit():
    print(f"Depositing now...")
def withdraw():
    print(f"Withdrawing now...")

#Evan's Code:
'''
Balance Check

Objective: Create a module to check the current balance of any user's account.

Key Functions:
    1.) Ask the user for their account details (name and PIN).
    2.) Display the current balance.
    3.) Include validation to ensure that only the correct PIN provides access to the account.
'''
def check_balance():
    print(f"Checking balance now...")

#Makai's Code:
'''
Money Transfer System

Objective: Implement a money transfer function that allows users to transfer money between accounts.

Key Functions:
    1.) Ask the user for their account details and the account details of the person they want to transfer money to.
    2.) Ensure sufficient funds exist before transferring money.
    3.) Deduct from one account and add to the other.
'''
def transfer():
    print(f"Transfering funds now...")

#Taylor's Code:
'''
Transaction History and Reports

Objective: Write a module that generates a simple report of transactions (deposits, withdrawals, transfers).

Key Functions:
    1.) Log each transaction (type of transaction, amount, date/time).
    2.) Provide a way for users to view a history of their transactions.
'''
def check_history():
    print(f"Checking history now...")

#Main Menu:
#This will introduce the user to our code and prompt for a selection of what the user would like to do.
print(f"Hello there! Welcome to B-Rad Banking Inc.\n")
print(f"What would you like to do?\n\nCreate New Account\nDeposit/Withdraw\nCheck Balance\nTransfer Money\nCheck Transaction History")
while(main_menu): #Loop until a valid selection is given
    main_menu = False
    selection = input(f'\nPlease input "create", "deposit", "withdraw", "check balance", "transfer", or "check history": ')
    if selection.lower() == "create":
        create() #Run Austin's code
    elif selection.lower() == "deposit":
        deposit() #Run Brad's code
    elif selection.lower() == "withdraw":
        withdraw() #Run Brad's code
    elif selection.lower() == "check balance":
        check_balance() #Run Evan's Code
    elif selection.lower() == "transfer":
        transfer() #Run Makai's Code
    elif selection.lower() == "check history":
        check_history() #Run Taylor's Code
    else:
        print(f"We're sorry, that is not a valid input, try again please!")
        main_menu = True
