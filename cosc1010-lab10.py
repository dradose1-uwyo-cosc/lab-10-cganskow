# Caitlyn Ganskow
# UWYO COSC 1010
# 11/21/24
# Lab 10
# Lab Section: 12 
# Sources, people worked with, help given to: None

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.
try:
    path_hash = Path('hash')
    content_hash = path_hash.read_text()
except:
    print('hash file not found')

# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

try:
    path_rock = Path('rockyou.txt')
    content_rock = path_rock.read_text()
except: 
    print("file not found")

for line in content_rock:
    if get_hash(line) == content_hash:
        print(f"The password is {line}")
        break
    else:
        print("no")