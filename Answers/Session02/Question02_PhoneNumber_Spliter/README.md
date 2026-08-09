# Extract Three Number After Zero

## Description

This is a simple Python program that receives an 11-digit phone number from the user and extracts the three numbers after zero.

For example, if the user enters:


09123456789


The program extracts:


912


and displays:


Three number after zero = 912


## How It Works

1. The user enters a phone number using `input()`.
2. The program uses string slicing to select the required numbers.
3. The extracted numbers are stored in a variable.
4. The result is displayed using an f-string.

## Concepts Used

This project practices:

- `input()` function
- String indexing
- String slicing
- f-string formatting
- Working with strings

## Example

### Input:

09123456789


### Output:

Three number after zero = 912


## Code Logic

```python
phone = input("Enter your phone number: ")

data = phone[1:4]

print(f"Three number after zero = {data}")
Explanation

phone[1:4] means:

Start from index 1
Stop before index 4
Extract three characters

Because the first digit (0) is located at index 0, the program extracts the next three numbers after zero.

Purpose

This project was created to practice Python basics, especially indexing, slicing, and formatted output using f-strings.

Author

Alireza
