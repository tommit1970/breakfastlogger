import sys

#standard out - sys.stdout

print(type(sys.stdout))
sys.stdout.write('Hello\n')

print(type(sys.stderr))
sys.stderr.write('Error messages can go here\n')

print(type(sys.stdin))
letter = sys.stdin.read(1)
print(letter)