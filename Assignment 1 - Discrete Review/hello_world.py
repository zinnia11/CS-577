import sys

next(sys.stdin)
for line in sys.stdin:
    print(f'Hello, {line.rstrip()}!')