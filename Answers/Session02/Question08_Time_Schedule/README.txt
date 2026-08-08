# Time Period Identifier

A simple Python program that receives a time from the user in **24-hour format** and displays the corresponding **12-hour format** with **AM/PM** and the appropriate time period.

## Features

* Accepts time in **24-hour format**.
* Converts the time to **12-hour format**.
* Displays **AM** or **PM**.
* Identifies the time period:

  * Morning
  * Afternoon
  * Evening
  * Night
* Validates the entered time and displays an error message if the input is invalid.

## How to Use

Run the program and enter the time in the following format:

```text
HH:MM
```

**Important:**

* Enter the **hour** first.
* Type a **colon (`:`)** between the hour and the minute.
* Then enter the **minute**.
* The hour must be between **0 and 23**.
* The minute must be between **0 and 59**.

### Valid Examples

```text
09:30
```

```text
14:45
```

```text
23:10
```

```text
00:05
```

### Invalid Examples

```text
25:10
```

```text
12:75
```

```text
9-30
```

```text
0930
```

## Example Output

**Input**

```text
09:30
```

**Output**

```text
9:30 AM (Morning)
```

---

**Input**

```text
18:20
```

**Output**

```text
6:20 PM (Evening)
```

## Technologies Used

* Python
* Conditional Statements (`if`, `elif`, `else`)
* String Manipulation (`split`)
* Type Conversion (`int`)
* Formatted Strings (f-strings)
