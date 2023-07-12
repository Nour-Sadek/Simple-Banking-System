import random
import sqlite3

conn = sqlite3.connect('card.s3db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS card (
id INTEGER PRIMARY KEY AUTOINCREMENT,
number TEXT,
pin TEXT,
balance INTEGER DEFAULT 0)""")


class CreditCard:
    """Credit cards of a bank

    Attributes:

    card_number: an int representing a 16-digit credit card number
    pin: an int representing a 4-digit number
    balance: an int representing the balance this card has
    credit_cards_can: a list representing a class instance that saves the
    Customer Account NUmber (CAN) of all cards registered in the system
    credit_cards: a dictionary where the key represents the card number and
    the value is the CreditCard class to which this card number belongs to

    """
    card_number: str
    pin: str
    balance: int
    can: str

    def __init__(self, card_number: str, pin: str) -> None:
        self.card_number = card_number
        self.pin = pin
        self.balance = 0
        self.can = card_number[6:-1]

    def add_income(self) -> None:
        while True:
            income = input('\nEnter income: ')
            try:
                income = int(income)
            except ValueError:
                print('Please provide a number')
            else:
                if income < 0:
                    print('Please provide a valid positive income.')
                else:
                    self.balance = self.balance + income
                    print('Income was added!\n')
                    break


class Bank:
    """A bank that issues credit cards to customers.

    cards: A dictionary that maps a credit's card number (key) to a CreditCard
           object
    """

    cards: dict[str, CreditCard]
    cards_can: list[str]

    def __init__(self) -> None:
        self.cards = {}
        self.cards_can = []

    def add_card(self, card: CreditCard) -> None:
        card_number = card.card_number
        card_can = card.can
        self.cards[card_number] = card
        self.cards_can.append(card_can)


# Helper functions
def welcome_message() -> str:
    return f'''1. Create an account
2. Log into account
0. Exit  
'''


def account_message() -> str:
    return f'''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
'''


def create_can() -> str:
    """Return a unique Customer Account Number (CAN)."""

    CAN_list = [str(random.choice(range(10))) for _ in range(9)]
    CAN = ''.join(CAN_list)
    if CAN in bank.cards_can:
        CAN = create_can()
    return CAN


def create_check_sum(BIN: str) -> str:
    """Return a one digit check_sum whose addition to the 15 digit <BIN> will
    satisfy the Luhn algorithm."""

    # Create a dictionary where each digit of BIN corresponds to a step,
    # starting from 1
    BIN_dict = {key: int(value) for key, value in enumerate(BIN, start=1)}
    # Multiply digits that correspond to odd steps by 2
    BIN_dict = {key: (value*2 if key % 2 == 1 else value) for key, value in \
                BIN_dict.items()}
    # Subtract 9 from digits that are over 9
    BIN_list = [value - 9 if value > 9 else value for value in \
                list(BIN_dict.values())]
    # Add all numbers
    sum_all = sum(BIN_list)
    # The 16th digit is the digit where, once it is added to <sum_all> leads to
    # a number divisible by 10
    num = int(str(sum_all)[-1])
    if num == 0:
        last_digit = 0
    else:
        last_digit = 10 - num
    return str(last_digit)


def create_card_number() -> str:
    """Return a unique credit card number that specifies the following
    requirements:

    - Issuer Identification Number (IIN) is 400000
    - Customer Account Number (CAN) is a unique 9 digit number that doesn't
    already exist in CreditCard class.
    - Checksum is a number that will satisfy the Luhn algorithm.
    """

    IIN = '400000'
    CAN = str(create_can())
    check_sum = create_check_sum(IIN + CAN)
    card_number = IIN + CAN + check_sum
    return card_number


def create_pin() -> str:
    """Return a Personal Identification Number (PIN) that can take any value
    between 0000 and 9999."""

    pin_list = [str(random.choice(range(10))) for _ in range(4)]
    pin = ''.join(pin_list)
    return pin


def create_card() -> CreditCard:
    card_number = create_card_number()
    pin = create_pin()
    card = CreditCard(card_number, pin)
    command = f'INSERT INTO card (number, pin) VALUES ({card_number}, {pin})'
    c.execute(command)
    conn.commit()
    return card


def check_account(card: CreditCard) -> None:
    while True:
        print(account_message())
        user_input = input()
        if user_input == '1':  # Check balance
            print(f'Balance: {card.balance}\n')
        elif user_input == '2':  # Add income
            card.add_income()
        elif user_input == '3':  # Make a transfer
            pass
        elif user_input == '4':  # Close account
            # Delete account from database
            command = f'DELETE FROM card WHERE number = {card.card_number}'
            c.execute(command)
            conn.commit()
            # Delete account from Bank
            del bank.cards[card.card_number]
            bank.cards_can.remove(card.can)
            break
        elif user_input == '5':  # Log out
            print('\nYou have successfully logged out!\n')
            break
        elif user_input == '0':  # Exit
            print('Bye!')
            quit()
        else:
            print('Wrong Input. Try again.\n')


bank = Bank()

while True:
    print(welcome_message())
    user_input = input()

    if user_input == '0':
        print('Bye!')
        break

    elif user_input == '1':

        card = create_card()
        bank.add_card(card)

        print(f'''Your card has been created
Your card number:
{card.card_number}
Your card PIN:
{card.pin}\n''')

    elif user_input == '2':
        user_input_number = input('Enter your card number: ')
        user_input_pin = input('Enter your pin: ')
        if user_input_number not in bank.cards:
            print('\nWrong card number!\n')
        else:
            if bank.cards[user_input_number].pin != user_input_pin:
                print('\nWrong pin to Credit Card!\n')
            else:
                print('\nYou have successfully logged in!\n')
                card = bank.cards[user_input_number]
                check_account(card)
    else:
        print('Wrong Input. Try again.\n')
