# To understand how sys function works ...

import sys

# It takes input as input() works ,
# Difference is, they automatically generates \n after completion
for line in sys.stdin:
    if 'q' in line.rstrip():
        break
    print(f'Input: {line}')

print("Exit")
