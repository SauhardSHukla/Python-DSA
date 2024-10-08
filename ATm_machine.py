# ATM Machine Simulation in Python
##Code holds various function that perform to make all the step of completion of ATM Machine 


class ATMMachine:
    def __init__(self, initial_balance=1000, pin=1234):
        """
        Constructor to initialize the account with balance and PIN.
        Transaction history is stored as a list of strings.
        """
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []
    
    def check_pin(self):
        max_try = 3  # Maximum number of attempts
        try_no = 0  

        while try_no < max_try:
            entered_pin = input("Enter your PIN: ").strip()  

            if entered_pin == "":  
                print("PIN cannot be empty!")
            else:
                try:
                    entered_pin = int(entered_pin) 
                except ValueError:
                    print("Invalid PIN! Please enter a numeric PIN.")
                    continue  

                if entered_pin == self.pin:  # Check if PIN matches
                    return True  # Correct PIN, exit the function
                else:
                    print("Incorrect PIN!")

            try_no += 1  

        print("Too many incorrect attempts. Access denied.")
        return False  # all attempts denied         

    def balance_inquiry(self):
        """
        Function to display the current balance in the account.
        """
        print(f"Your current balance is: {self.balance}")
        self.transaction_history.append(f"Balance Inquiry: {self.balance}")

    def withdraw(self, amount):
        """
        Function to withdraw cash from the account.
        It checks if the amount to be withdrawn is less than or equal to the balance.
        """
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! You withdrew {amount}.")
            self.transaction_history.append(f"Withdrawn: {amount}")
    
    def deposit(self, amount):
        """
        Function to deposit cash into the account.
        """
        self.balance += amount
        print(f"Deposit successful! You deposited {amount}.")
        self.transaction_history.append(f"Deposited: {amount}")
    
    def change_pin(self):
        """
        Function to change the user's PIN.
        It prompts the user to enter the current and new PIN, and updates the PIN if correct.
        """
        if self.check_pin():
            new = int(input("Enter your new PIN: "))
            self.pin = new
            print("PIN changed successfully!")
            self.transaction_history.append("PIN changed")
    
    def show_transaction_history(self):
        """
        Function to display the transaction history.
        """
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

    def atm_menu(self):
        """Function to display the ATM menu and allow the user to select operations.It ensures that the user enters a correct PIN before proceeding with any action."""
        if self.check_pin():
            while True:
                print("\nATM Menu")
                print("1. Balance Inquiry")
                print("2. Cash Withdrawal")
                print("3. Cash Deposit")
                print("4. Change PIN")
                print("5. Transaction History")
                print("6. Exit")
            
                try:
                    choice = input("Enter your choice: ").strip()  # Removes extra spaces
                    if choice == "":  # Check if input is empty
                        raise ValueError("Empty input...")  # Trigger ValueError
                    choice = int(choice)  # Convert to integer if not empty
                    if choice == 1:
                        self.balance_inquiry()
                    elif choice == 2:
                        amount = int(input("Enter the amount to withdraw: "))
                        self.withdraw(amount)
                    elif choice == 3:
                        amount = int(input("Enter the amount to deposit: "))
                        self.deposit(amount)
                    elif choice == 4:
                        self.change_pin()
                    elif choice == 5:
                        self.show_transaction_history()
                    elif choice == 6:
                        print("Exiting... Thank you for using the ATM!")
                        break
                    else:
                        print("Invalid choice! Please enter a number between 1 and 6.")
            
                except ValueError as Empty_value :
                    print(f"Error!!!!! {Empty_value} You have not entered any value over here")


      


# Main function to start the ATM Machine interface
def main_function():
    atm = ATMMachine()  
    atm.atm_menu()

if __name__ == "__main__":
    main_function()
