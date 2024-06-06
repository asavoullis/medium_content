import sys

# Managing Recursion Limits with sys.getrecursionlimit() and sys.setrecursionlimit()

# Print the current recursion limit
print("Current recursion limit:", sys.getrecursionlimit())

# Set a new recursion limit
sys.setrecursionlimit(2000)
print("New recursion limit:", sys.getrecursionlimit())

# Measuring Object Size with sys.getsizeof()

# Create an integer object
a = 42
# Print the size of the integer object in bytes
print("Size of integer object:", sys.getsizeof(a))

# Create a string object
b = "Hello, World!"
# Print the size of the string object in bytes
print("Size of string object:", sys.getsizeof(b))

# Create a list object
c = [1, 2, 3, 4, 5]
# Print the size of the list object in bytes
print("Size of list object:", sys.getsizeof(c))

# Inspecting Imported Modules with sys.modules

# Import the math module
import math

# Print the list of currently imported modules
print("Modules currently imported:", list(sys.modules.keys()))

# Check if a specific module (math) is imported
if 'math' in sys.modules:
    print("Math module is imported")

# Advanced Error Handling with sys.exc_info()

try:
    # Cause a ZeroDivisionError exception
    1 / 0
except ZeroDivisionError:
    # Retrieve exception information
    exc_type, exc_value, exc_traceback = sys.exc_info()
    # Print exception type
    print("Exception type:", exc_type)
    # Print exception value
    print("Exception value:", exc_value)
    # Print exception traceback
    print("Exception traceback:", exc_traceback)

# Identifying the Platform with sys.platform

# Print the platform on which Python is running
print("Platform:", sys.platform)

# Check the platform and print corresponding messages
if sys.platform.startswith('linux'):
    print("Running on Linux")
elif sys.platform == 'darwin':
    print("Running on macOS")
elif sys.platform == 'win32':
    print("Running on Windows")

# Managing References with sys.getrefcount()

# Create a list object
a = []
# Print the reference count for the list object
print("Reference count for the list object:", sys.getrefcount(a))

# Create another reference to the list object
b = a
# Print the reference count after creating another reference
print("Reference count after creating another reference:", sys.getrefcount(a))

# Customizing Standard Streams with sys.stdin, sys.stdout, and sys.stderr

# Define a custom stdout class
class CustomStdout:
    def write(self, message):
        # Custom processing of the message
        print(f"Custom Output: {message.strip()}")

    def flush(self):
        pass

# Replace the standard output with CustomStdout
sys.stdout = CustomStdout()

# Print a message that will be processed by CustomStdout
print("This will be processed by CustomStdout")

# Understanding System Byte Order with sys.byteorder

# Print the byte order of the system
print("Byte order of the system:", sys.byteorder)
