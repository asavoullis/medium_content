import sys

# for example let's execute: python sys_basics.py hello there

# sys.argv is a list where the first element is the script name
print("Script name:", sys.argv[0]) # Output sys_basics.py

# The rest are the arguments passed to the script
print("Arguments:", sys.argv[1:]) # Ouput: ['hello', 'there']

# prints the first argument passed after the script name
print(sys.argv[1]) # Output: hello


if len(sys.argv) < 2:
    print("No arguments provided. Exiting.")
    sys.exit()

# Save the original standard output
original_stdout = sys.stdout

# Redirect standard output to a file
with open('output.txt', 'w') as f:
    sys.stdout = f
    print("This will be written to the file.")

# Restore the original standard output
sys.stdout = original_stdout
print("This will be printed on the console.")