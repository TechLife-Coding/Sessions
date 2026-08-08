# Reverse Card Number

## Description

This is a simple Python program that receives a card number from the user and reverses the order of its digits using string slicing.

The program keeps the card number as a string because card numbers are identifiers, not values used for mathematical calculations.

## How It Works

1. The user enters a card number.
2. The input is stored in the `card_number` variable.
3. The program uses slicing with a negative step to reverse the card number.
4. The reversed card number is displayed in the output.

## Concepts Used

This project practices:

- `input()` function
- String data type
- String slicing
- Negative step (`step = -1`)
- Variables
- Output with `print()`

## Example

### Input:

```
1234567890
```

### Output:

```
0987654321
```

## Code Logic

```python
card_number = input("Enter card number: ")

reversed_numbers = card_number[::-1]

print(reversed_numbers)
```

## Explanation

`card_number[::-1]` uses Python slicing:

- Start: empty → start from the beginning
- Stop: empty → go until the end
- Step: `-1` → move backward one character at a time

Using `-1` reverses the order of the characters in the string.

## Why Use String Instead of Integer?

Card numbers are not used for mathematical calculations. They are identifiers.

Keeping them as strings prevents problems such as removing leading zeros.

Example:

```
0123456789
```

If converted to an integer:

```
123456789
```

The first zero would be removed.

## Purpose

This project was created to practice Python slicing, especially using negative steps to reverse strings.

## Author

Alireza
