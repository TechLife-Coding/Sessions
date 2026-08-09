# Find Largest Number

## 📌 Project Description

This is a simple Python program that finds the largest number in a list.

The program starts by assuming that the first number in the list is the largest. It then checks every number in the list and updates the largest value whenever it finds a bigger number.

---

## 🧠 How It Works

First, a list of numbers is created:

`python
numbers = [15, 50, 70, 1, 90, 20, 4, 100, 6]
Then the first element of the list is stored as the initial largest number:
larger_num = numbers[0]
The program loops through all the numbers:
for num in numbers:
For each number, it checks whether it is greater than the current largest number:
if num > larger_num:
    larger_num = num
If a larger number is found, larger_num is updated.
Finally, the largest number is printed:
print(larger_num)
💻 Example Output
For the following list:
[15, 50, 70, 1, 90, 20, 4, 100, 6]
The output will be:
100
🛠️ Technologies Used
Python 3
Lists
for loops
if statements
Comparison operators
Variables
▶️ How to Run
Make sure Python 3 is installed on your computer.
Run the program with:
python larger-number.py
The program will check all numbers in the list and print the largest one.
📂 Project Structure
Find-Largest-Number/
│
├── larger-number.py
└── README.md
🎯 Project Goal
This project is designed to practice basic Python concepts, including:
Working with lists
Understanding list indexing
Using for loops
Comparing values
Updating variables
Finding the maximum value manually
👨‍💻 Author :
Alireza Bahramifar
