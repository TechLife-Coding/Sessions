# Name and ID Separator

## Description
This is a simple Python program that receives a user's name and ID as a single connected string, then separates them using string slicing.

The program extracts:
- Name part
- ID part

and displays them separately in the output.

## How It Works
The user enters a string containing a name and an ID together.

Example:


Alireza1234567890


The program uses slicing to separate the two parts:

- The last 10 characters are considered the ID.
- The remaining characters are considered the name.

## Concepts Used
This project practices some basic Python concepts:

- `input()` for receiving user data
- String indexing
- String slicing
- Negative indexing
- Type casting using `int()`
- String formatting

## Example

### Input:

Alireza1234567890


### Output:

Name: Alireza
ID: 1234567890


## Notes
The program uses slicing:

```python
id = int(data[-10:])
name = data[:-10]

data[-10:] extracts the last 10 characters.

data[:-10] extracts everything before the last 10 characters.

Author

Alireza
