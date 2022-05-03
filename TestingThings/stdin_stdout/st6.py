from io import StringIO
import sys

temp_output = StringIO()

# Replace stdout with the StringIO object
sys.stdout = temp_output
# Now, if you print() or use sys.stdout.write
# it goes to the string objc
print('This is going to the StringIO obecjt.')
sys.stdout.write('This is not going to the "real" stdout, yet')

# Then we can restore original stdout
sys.stdout = sys.__stdout__
print("Contents of the StringIO object")
print("===============================")
print(temp_output.getvalue())