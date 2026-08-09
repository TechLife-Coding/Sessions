# 🏃 Jumper Calculator

A simple Python program that tracks an athlete's jump performance over 10 attempts.

The program compares each new jump with the previous jump and tells the athlete whether they:
- 🏆 Set a new record
- 📈 Jumped higher than before
- 📉 Jumped lower than before
- ➖ Stayed on the same record

## 🚀 Features

- Takes 10 jump inputs from the user
- Compares the current jump with the previous jump
- Calculates the difference between jumps
- Displays a motivational message for each result
- Supports decimal values using float

## 🧠 How It Works

The program keeps two main values:

- oldrec → The previous jump
- newrec → The current jump

For every attempt, the program compares:

`python
newrec > oldrec
If the new jump is higher, the program calculates how much higher it is.
If:
newrec == oldrec
the athlete stayed on the same record.
If:
newrec < oldrec
the program calculates how much lower the new jump was.
At the end of each attempt:
oldrec = newrec
The current jump becomes the previous jump for the next attempt.
💻 Example
Input:
33
34
8
8
Output:
Old record was 33 M, and new record is 34 M.
Great job! You jumped 1 M higher!

Old record was 34 M, and new record is 8 M.
You jumped -26 M less. Try harder!

Old record was 8 M, and new record is 8 M.
Same record. Try harder!
🛠️ Technologies
Python 3
for loop
if / elif
float()
input()
f-strings
📚 What I Learned
This project helped me practice:
Variables
Loops
Conditional statements
Comparing values
Updating variables
Basic calculations
User input
f-strings
🎯 Future Improvements
Possible improvements for future versions:
Store all 10 jumps in a list
Show the highest jump at the end
Show the average jump
Count how many records were broken
Add a final performance summary
Add input validation
👨‍💻 Project Status
Completed — Beginner Python Project
Built to practice Python fundamentals and problem-solving.

## Author:
   Alireza Bahramifar