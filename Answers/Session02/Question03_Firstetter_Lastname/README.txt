# Display First Letter of Name and Full Last Name

## Description

This is a simple Python program that receives a user's first name and last name as a single input.

The program extracts:
- The first letter of the first name.
- The complete last name.

Finally, it displays the result in the following format:

```
A.Bahramifar
```

## How It Works

1. The user enters their first name and last name.
2. The program stores the first character of the name in a separate variable.
3. It finds the space between the first name and last name.
4. Using string slicing, it extracts the last name.
5. The result is displayed using an f-string.

## Concepts Used

This project practices:

- `input()` function
- String indexing
- String slicing
- `find()` function
- Variables
- f-string formatting

## Example

### Input

```
Alireza Bahramifar
```

### Output

```
A.Bahramifar
```

## Code Logic

```python
full_name = input("Enter your name and family: ")

first_letter = full_name[0]

space = full_name.find(" ")

last_name = full_name[space + 1:]

print(f"{first_letter}.{last_name}")
```

## Explanation

- `full_name[0]` extracts the first character of the first name.
- `find(" ")` finds the position of the space between the first name and last name.
- `space + 1` starts from the first character of the last name.
- `last_name = full_name[space + 1:]` extracts the entire last name.
- The final result is displayed using an f-string.

## Purpose

This project was created to practice Python string indexing, slicing, the `find()` function, variables, and formatted output using f-strings.

## Author

Alireza
