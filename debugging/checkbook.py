class Checkbook:
    """A simple checkbook application for managing a personal account balance."""

    def __init__(self):
        """Initializes a new checkbook with a balance of zero."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.
        
        Parameters:
            amount (float): The amount to be deposited.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if sufficient funds are available.
        
        Parameters:
            amount (float): The amount to be withdrawn.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Prints the current balance of the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """Main function to run the checkbook application."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
