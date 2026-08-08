# 🏦 Bank Prefix (Dictionary Version)

A simple Python program that identifies the issuing bank of an Iranian bank card using a Python dictionary.

## Features

- Receives a 16-digit bank card number from the user.
- Extracts the first four digits (bank prefix).
- Stores bank prefixes and names in a Python dictionary.
- Checks whether the prefix exists in the dictionary.
- Displays the corresponding bank name.

## Supported Banks

- Blue Bank
- Pasargad Bank
- Resalat Bank
- Saderat Bank
- Tejarat Bank
- Refah Bank
- Mellat Bank
- Ayandeh Bank
- Shahr Bank
- Parsian Bank

## How It Works

1. The user enters a bank card number.
2. The program extracts the first four digits using string slicing.
3. It searches for the prefix in a dictionary.
4. If the prefix exists, the bank name is displayed.

## Example

**Input**

```text
BANK ACC: 5022211456784210
```

**Output**

```text
Pasargad Bank: 5022
```

## Concepts Used

- Python Dictionary
- Dictionary Lookup
- Membership Operator (`in`)
- String Slicing
- f-Strings

## Author

Alireza Bahramifar
