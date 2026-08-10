Color Similarity Checker — Beginner Alternative

An alternative version of the Color Similarity Checker project.

This version solves the same problem as the Beginner version, but uses "set()" and "len()" to make the comparison shorter and cleaner.

📁 Project Structure

Beginner_Alternative/
└── ColorsCombiner_Alternative.py

📌 How It Works

The program asks the user to enter three colors using a "for" loop and stores them in a list.

Then, "set()" removes duplicate colors, while "len()" counts the number of unique colors.

🔹 Possible Results

- If all three colors are the same:
  
  Three colors same

- If two colors are the same:
  
  Same

- If all three colors are different:
  
  No colors are the same

🧠 Example

Input:

Choose a color: red
Choose a color: blue
Choose a color: red

The list contains:

["red", "blue", "red"]

After using "set()":

{"red", "blue"}

There are 2 unique colors, so the output is:

Same

🎯 Concepts Used

- "for" loop
- "list"
- "string"
- "input()"
- "set()"
- "len()"
- "if"
- "elif"
- "else"

🔄 Difference From Beginner Version

The Beginner version compares the colors directly using their list indexes.

The Beginner Alternative version uses "set()" and "len()" to detect repeated colors without directly comparing each list index.

👨‍💻 Author

Alireza Bahramifar
