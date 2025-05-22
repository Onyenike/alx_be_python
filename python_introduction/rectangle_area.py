Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> lenght = 10
>>> width = 5
>>> area = lenght * width
>>> print("The area of the rectangle is:" area)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> lenght = 10
... width = 5
... area = lenght * width
... print("The area of the rectangle is:" + area)
SyntaxError: multiple statements found while compiling a single statement
>>> lenght = 10
... width = 5
... area = lenght * width
... print("The area of the rectangle is: " + str (area))
SyntaxError: multiple statements found while compiling a single statement
>>> lenght = 10
... width = 5
... area = lenght * width
... print("The area of the rectangle is: " + area)
SyntaxError: multiple statements found while compiling a single statement
>>> lenght = 10
>>> width = 5
>>> area = lenght * area
>>> lenght = 10
>>> width = 5
>>> area = lenght * width
>>> print("The area of the rectangle is: " + str(area))
The area of the rectangle is: 50
