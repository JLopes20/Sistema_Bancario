balance = 0
limit = 500
statement = ""
MAX_DAILY_WITHDRAW = 3
withdraw_count = 0

while True:
    user_transaction = input("Enter 'd' for deposit, 'w' for withdraw, 's' for statement, or 'q' to quit: ")

    if user_transaction == "d":
        deposit = float(input("Input the deposit amount desired: $ "))
        if deposit > 0:
            balance = balance + deposit
            statement = statement + "Deposit of: $" + str(deposit) + "\n"

    elif user_transaction == "w":
        
        if withdraw_count <= MAX_DAILY_WITHDRAW:
            withdrawal = float(input("Input the withdrawal amount: $ "))
            if withdrawal > 0 and withdrawal <= balance and withdrawal <= limit:
                balance = balance - withdrawal
                statement = statement + "Withdrawal of: $" + str(withdrawal) + "\n"
                withdraw_count += 1
            else:
                print("Invalid withdrawal amount. Please try again.")
        else:
            print("You have reached the maximum number of daily withdrawals.")

    elif user_transaction == "s":
        print("Your current balance: $", balance)
        print("Transaction Statement:")
        print(statement)

    elif user_transaction == "q":
        print("Thank you for using our banking application. Goodbye!")
        break

    else:
        print("Invalid input. Please try again.")
