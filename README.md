# Simple Banking System

### About
A user can create a bank account at the start menu, where a card number and its
pin will be automatically generated for the user.

A card number is made up of an Issuer Identification Number IIN (here, it is 400000), 
a Customer Account Number CAN (here, a unique 9-digit number), and a check digit 
that makes sure the number of the card is valid using the Luhn algorithm. Each 
created card number will fit this description.

If the user wishes to log into an account, they will have to input a valid card 
number and pin (i.e. one which was already automatically created). After that, the 
user has 6 options:

1 - Balance: The user can check the balance available in the account

2 - Add income: The user can add any amount of valid positive income to the account

3 - Do transfer: The user can attempt to transfer from this account to another already created
account a valid amount of money

4 - Close account: This will delete the account

5 - Log out: This will log out the user from the current account.

0 - Exit: This will exit the user from the program.

To avoid the data disappearing after the completion of the program, every 
created account will be stored in a database (using sqlite3) so that they are 
accessible during every run of the program.

This simple database will store a single table `card` with the following columns:
`(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)`.

### Learning Outcomes
Find out how the banking system works and learn about SQL and databases. See 
how the Luhn algorithm can help us avoid mistakes when entering the card 
number and learn basic OOP concepts such as classes.

# General Info

To learn more about this project, please visit 
[HyperSkill Website - Simple Banking System](https://hyperskill.org/projects/109).

This project's difficulty has been labelled as __Hard__ where this is how 
HyperSkill describes each of its four available difficulty levels:

- __Easy Projects__ - if you're just starting
- __Medium Projects__ - to build upon the basics
- __Hard Projects__ - to practice all the basic concepts and learn new ones
- __Challenging Projects__ - to perfect your knowledge with challenging tasks

This Repository contains one .py file:

    bank.py - Contains the code used to achieve the program's purpose

Project was built using python version 3.11.3

# How to Run

Download the bank.py file to your local repository and open the project in your choice 
IDE and run the project. After a single run of the program, a database card.s3db would 
have been created in the same working directory.
