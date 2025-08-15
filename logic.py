from PyQt6.QtWidgets import *
from  login_page import *
from data_handler import *
from accounts import *

class Logic(QMainWindow, Ui_login_page):
    """
        GUI class for Login & Account details page, this screen would switch between Login and Account pages.

        Handles user login whereas Account page for transactions (deposit/withdraw), and update the CSV file.
    """
    def __init__(self) -> None:
        """
        Initializes the Logic GUI class, sets up the interface,
        initializes user/account variables, and connects buttons to functions.
        """
        super().__init__()
        self.setupUi(self)

        self.account_hide()

        self.__balance = 0.0
        self.__index = -1
        self.__acct_number = 0
        self.__acct_name = ''

        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.Login_pb.clicked.connect(lambda : self.submit())
        self.Enter_pb.clicked.connect(lambda: self.transaction())

    def submit(self) -> None:
        """
        Handles user login.

        Validates username and password, checks with the CSV file,
        and shows/hides GUI elements when logged successfully.
        """
        username = self.input_Username.text().strip().lower()
        password = self.input_password.text().strip().lower()

        self.label_info.setText('')

        if username == '':
           self.label_info.setText('Please enter your username')
        elif password == '':
           self.label_info.setText('Please enter your password')
        else:
            with open('user_account.csv', 'r', newline='') as csvfile:

                reader = csv.reader(csvfile)
                header = next(reader)
                for column in reader:
                    if username != column[1] or password != column[2]:
                        self.label_info.setText('Wrong username or password')
                        self.input_Username.setText('')
                        self.input_password.setText('')
                    else:
                        self.__index += 1
                        self.__balance = float(column[4])
                        self.__acct_number = column[3]
                        self.__acct_name = column[0]

                        self.login_hide()
                        self.account_show()

    def transaction(self) -> None:
        """
        Processes a deposit or withdrawal transactions.

        Validates the input amount, checks which transaction type is selected,
        updates the account balance, updates the CSV file, and displays output messages.
        Deselects the radio button after the transaction.
        """
        try:
            self.label_output_message.setText(" ")
            amount = float(self.amount_input.text().strip())

            if amount <= 0:
                self.label_output_message.setText("Amount must be positive")
                return
            elif self.deposit_rb.isChecked():
                self.deposit(self.__index, self.__acct_number, float(self.label_balance.text()), float(self.amount_input.text()))
            elif self.withdraw_rb.isChecked():
               self.withdraw(self.__index, self.__acct_number, float(self.label_balance.text()), float(self.amount_input.text()))
            else:
               self.label_output_message.setText("Please select transaction type")
               return

            self.amount_input.clear()
            if self.transaction_group.checkedButton() is not None:
                self.transaction_group.setExclusive(False)
                self.transaction_group.checkedButton().setChecked(False)
                self.transaction_group.setExclusive(True)
        except ValueError:
            self.label_output_message.setText("Please enter numeric value")
        except TypeError:
            self.label_output_message.setText("Please enter numeric value")

    def deposit(self, index, acc_number, acc_balance, deposit_amount) -> None:
        """
        Deposit an amount into the account and updates the balance.
        Args:
            index(int): Row index of the account in the CSV file.
            acc_number: The account number.
            acc_balance(float) :  Current balance of the account.
            deposit_amount(float) : Amount to deposit.

        Returns:
        None
        """
        current_account = Account(acc_number, acc_balance)

        if current_account.deposit(float(deposit_amount)):
            balance = current_account.get_balance()
            self.label_balance.setText(f"{balance:.2f}")
            update_csv_value('user_account.csv', index, 'Balance', balance)
            self.label_output_message.setText("Deposit successful")
        else:
            self.label_output_message.setText("Deposit failed")

    def withdraw(self,index, acc_number, acc_balance, withdraw_amount) -> None:
        """
        Withdraws an amount from the account if sufficient balance exists.
        Args:
            index(int): Row index of the account in the CSV file.
            acc_number: The account number.
            acc_balance(float): current balance of the account.
            withdraw_amount(float): Amount to withdraw.

        Returns:
        None
        """
        acc1 = Account(acc_number, acc_balance)

        if withdraw_amount > acc_balance:
            self.label_output_message.setText("Insufficient balance")
            return

        if acc1.withdraw(float(withdraw_amount)):
            balance = acc1.get_balance()
            self.label_balance.setText(f"{balance:.2f}")
            update_csv_value('user_account.csv', index, 'Balance', balance)
            self.label_output_message.setText("Withdraw successful")
        else:
            self.label_output_message.setText("Withdraw failed")

    def login_hide(self) -> None:
        """
        Hides the login input fields and buttons after user login successfully.
        """
        self.input_Username.hide()
        self.input_password.hide()
        self.label_password.hide()
        self.label_Username.hide()
        self.label_info.hide()
        self.Login_pb.hide()
        self.setWindowTitle('Account')

    def account_hide(self) -> None:
        """
        Hides all account page GUI elements
        """
        self.label_accountholder.hide()
        self.label_accountusername.hide()
        self.label_accountnumber.hide()
        self.label_accountb.hide()
        self.label_user_account_number.hide()
        self.label_balance.hide()
        self.label_transaction.hide()
        self.deposit_rb.hide()
        self.withdraw_rb.hide()
        self.label_enter_amount.hide()
        self.amount_input.hide()
        self.Enter_pb.hide()
        self.label_output_message.hide()
        self.label_dollar.hide()

    def account_show(self) -> None:
        """
        Shows all account page GUI elements and updates labels with current account info.
        """
        self.label_accountholder.show()
        self.label_accountusername.show()
        self.label_accountusername.setText(self.__acct_name)

        self.label_accountnumber.show()
        self.label_accountb.show()
        self.label_user_account_number.show()
        self.label_user_account_number.setText(self.__acct_number)
        self.label_balance.show()
        self.label_balance.setText(f'{self.__balance}')
        self.label_dollar.show()

        self.label_transaction.show()
        self.deposit_rb.show()
        self.withdraw_rb.show()

        self.label_enter_amount.show()
        self.amount_input.show()
        self.Enter_pb.show()
        self.label_output_message.show()