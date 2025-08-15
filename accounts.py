class Account:
    """
     A class to represent a bank account with basic deposit and withdrawal functionality.

    Attributes:
        __account_number (str): Unique identifier for the account.
        __account_balance (float): Current account balance.
    """
    def __init__(self, account_number, balance=0) -> None:
        """
        Initialize a new Account instance.

        Args:
            account_number (str): Unique account identifier.
            balance (float): The starting balance and the value must be positive.
        """
        self.__account_number = account_number
        if balance > 0:
            self.__account_balance = balance
        else:
            self.__account_balance = 0
        self.set_balance(self.__account_balance)

    def deposit(self, amount) ->bool:
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit and value must be positive.

        Returns:
            bool: True if deposit was successful, False if amount is invalid or non-positive.
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        """
        Withdraw money from the account if sufficient balance exists.

        Args:
            amount (float): Amount to withdraw and the value must be positive.The value also has to be less than or equal to the current balance.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if (amount > 0) and (self.__account_balance >= amount):
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Get the current balance of the account.

        Returns:
            float: Current account balance.
        """
        return self.__account_balance

    def get_account_number(self) -> str:
        """
        Get the account number.

        Returns:
            str: The account's unique identifier.
        """
        return self.__account_number

    def set_balance(self, value) -> None :
        """
         Set the account balance.

        Args:
            value (float): New balance amount. Must be positive; otherwise balance is set to 0.
        """
        if value > 0:
            self.__account_balance = value
        else:
            self.__account_balance = 0

    def set_account_number(self, value) -> None:
        """
        Set the account number.

        Args:
            value (str): New account number.
        """
        self.__account_number = value