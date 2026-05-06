"""
File name: AccountingWhileLoop.py
Short description: Simple banking system simulation using a while loop.
IST 140 Assignment: AccountingWhileLoop
@author Jerry Khoutsavanh
@version 1.01 03/21/2025
date of last revision: 03/21/2025
details of the revision: none
"""

balance = 1000.00
choice = 0

while choice != 4 :
    print("\nEnter the number of your transaction type.")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Quit")
    choice = int(input("Enter choice: "))

    if choice == 1 :
        print("Your current balance is $%.2f." % balance)

    elif choice == 2 :
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Your current balance is $%.2f." % balance)

    elif choice == 3 :
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance :
            balance = balance - amount
            print("Your current balance is $%.2f." % balance)
        else :
            print("Insufficient funds. Your current balance is $%.2f." % balance)

    elif choice == 4 :
        print("Good-bye")

    else :
        print("Invalid menu choice.")

"""
Output 1:
Enter the number of your desired transaction type.
1. Balance
2. Deposit
3. Withdrawal
4. Quit
Enter choice: 1
Your current balance is $1000.00.

Enter the number of your desired transaction type.
1. Balance
2. Deposit
3. Withdrawal
4. Quit
Enter choice: 4
Good-bye

Output 2:
Enter the number of your desired transaction type.
1. Balance
2. Deposit
3. Withdrawal
4. Quit
Enter choice: 2
Enter deposit amount: 500.00
Your current balance is $1500.00.

Enter the number of your desired transaction type.
1. Balance
2. Deposit
3. Withdrawal
4. Quit
Enter choice: 4
Good-bye

Output 3:
Enter the number of your desired transaction type.
1. Balance
2. Deposit
3. Withdrawal
4. Quit
Enter choice: 3
Enter withdrawal amount: 2000.00
Insufficient funds. Your current balance is $1000.00.

Enter the number of your desired transaction type.
1. Balance
2. Deposit
3. Withdrawal
4. Quit
Enter choice: 4
Good-bye
"""