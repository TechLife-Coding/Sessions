# Taxi Fare Calculator

## Description
This Python program calculates the final taxi fare based on the distance traveled.

## Features
- Receives the traveled distance using the `way` variable.
- Accepts decimal (`float`) values.
- Uses `for _ in range(100)` to allow up to 100 calculations.
- Uses the `subprocess` module to clear the console after each calculation.
- Calculates the final taxi fare based on the given rules.
- Displays the entered distance and the final taxi fare using f-strings.

## Fare Rules
- If the distance is less than **2 km**, the fare is **$20**.
- Otherwise, the first **2 km** cost **$20**, and each additional kilometer costs **$5**.

## Python Concepts Used
- `import subprocess`
- `subprocess.run()`
- `input()`
- `float()`
- `for _ in range()`
- `if` / `elif`
- Variables
- Arithmetic operators (`+`, `-`, `*`)
- f-string formatting

## Author

Alireza Bahramifar
