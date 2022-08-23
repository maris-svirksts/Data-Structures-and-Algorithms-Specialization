#Uses python3

import sys
from functools import cmp_to_key

def compare(item1, item2):
    return int(str(item2) + str(item1)) - int(str(item1) + str(item2))

def largest_number(a):
    a = sorted(a, key=cmp_to_key(compare))

    return ''.join(a)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
