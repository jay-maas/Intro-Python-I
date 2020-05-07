"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print('command line arguements: ', sys.argv)

# Print out the OS platform you're using:
# YOUR CODE HERE
platValue = sys.platform

if platValue == 'linux':
    platStr = 'Linux'
elif platValue == 'win32':
    platStr = 'Windows'
elif platValue == 'cygwin':
    platStr = 'Windows/Cygwin'
elif platValue == 'darwin':
    platStr = 'Max OS X'

print('Current OS platform: ', platStr)

# Print out the version of Python you're using:
# YOUR CODE HERE
pyVer = sys.version_info
pyVerStr = f'v{pyVer.major}.{pyVer.minor}.{pyVer.micro}'
print('Current Python Version: ', pyVerStr)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('current proccess ID: ', os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print('current working directory: ', os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print('current machine login name: ', os.getlogin())