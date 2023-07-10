import random


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
    card_number: int
    pin: int
    balance: int
    credit_cards_can: list[int]

    credit_cards_can = []
    credit_cards = {}

    def __init__(self, card_number: int, pin: int) -> None:
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

        CAN = str(card_number)[6:-1]
        CreditCard.credit_cards_can.append(int(CAN))
        CreditCard.credit_cards[card_number] = self

# Helper functions
def welcome_message() -> str:
    return f'''1. Create an account
2. Log into account
0. Exit  
'''


def account_message() -> str:
    return f'''1. Balance
2. Log out
0. Exit
'''


def create_can() -> int:
    """Return a unique Customer Account Number (CAN)."""

    CAN_list = [str(random.choice(range(10))) for _ in range(9)]
    CAN = ''.join(CAN_list)
    CAN = int(CAN)
    if CAN in CreditCard.credit_cards_can:
        CAN = create_can()
    return CAN


def create_card_number() -> int:
    """Return a unique credit card number that specifies the following
    requirements:

    - Issuer Identification Number (IIN) is 400000
    - Customer Account Number (CAN) is a unique 9 digit number that doesn't
    already exist in CreditCard class.
    - Checksum is a random number between 0 and 9.
    """

    IIN = '400000'
    CAN = str(create_can())
    check_sum = str(random.choice(range(10)))
    card_number = IIN + CAN + check_sum
    return int(card_number)


def create_pin() -> int:
    """Return a Personal Identification Number (PIN) that can take any value
    between 0000 and 9999."""

    pin_list = [str(random.choice(range(10))) for _ in range(4)]
    pin = ''.join(pin_list)
    pin = int(pin)
    return pin


def create_card() -> CreditCard:
    card_number = create_card_number()
    pin = create_pin()
    card = CreditCard(card_number, pin)
    return card


while True:
    print(welcome_message())
    user_input = input()

    if user_input == '0':
        print('Bye!')
        break
    elif user_input == '1':
        card = create_card()
        card_number = card.card_number
        card_pin = card.pin
        print(f'''Your card has been created
Your card number:
{card_number}
Your card PIN:
{card_pin}''')
    elif user_input == '2':
        print('Enter your card number:')
        user_input_number = int(input())
        print('Enter your pin:')
        user_input_pin = int(input())
        if user_input_number not in CreditCard.credit_cards:
            print('Wrong card number or pin!')
        else:
            if CreditCard.credit_cards[user_input_number].pin != user_input_pin:
                print('Wrong card number or pin!')
            else:
                print('You have successfully logged in!')
                card = CreditCard.credit_cards[user_input_number]
                while True:
                    print(account_message())
                    user_input = input()
                    if user_input == '1':
                        print(f'Balance: {card.balance}')
                    elif user_input == '2':
                        print('You have successfully logged out!')
                        break
                    elif user_input == '0':
                        print('Bye!')
                        quit()
