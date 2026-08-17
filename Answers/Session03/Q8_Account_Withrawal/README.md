# Account Withdrawal System

A simple Python program that simulates an account withdrawal system.

## Description

This project allows the user to enter a withdrawal amount and checks whether the account has enough money.

The account starts with a balance of 500.

If the requested withdrawal is greater than the current account balance, the program asks the user to charge the account first.

The program also checks that the entered amounts are positive and valid.

## Features

- Initial account balance: 500
- Accepts withdrawal amounts from the user
- Checks whether the account has enough balance
- Allows the account to be charged when necessary
- Rejects invalid or non-positive amounts
- Displays the remaining account balance after a successful withdrawal
- Uses a for loop to allow multiple transactions

## How It Works

1. The account starts with 500.
2. The user enters a withdrawal amount.
3. If the amount is greater than the account balance, the program asks the user to charge the account.
4. The program checks whether the charge amount is valid.
5. If the withdrawal is successful, the withdrawal amount is subtracted from the account.
6. The program displays the withdrawn amount and the remaining balance.

## Technologies

- Python 3

## How to Run

Run the following command in your terminal:

`bash
python Account_Withdrawal.py
Then enter the requested amounts when prompted.
👨‍💻 Author
Alireza Bahramifar