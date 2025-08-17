print("Hello to the viewer");

# NOTE: Please comment/uncomment respectively to try all syntaxes one by one.

#1. Invalid Syntax
# print("Hello World"

#2. Indentation error
'''
def my_function():
print("This line has incorrect indentation")
'''

#3. Keyword error
'''
for = 10
print(for)
'''

#4. Bracket error
'''
my_list = [1, 2, 3, 4, 5
print("The list was created without a closing bracket")
'''

# Some valid code syntaxes

#1.
#print("Hello World")

#2. Complex Script
'''
import sys

def check_platform():
    platform = sys.platform
    if "win" in platform:
        print("Running on Windows OS.")
    else:
        print(f"Running on {platform}.")

check_platform()
'''
