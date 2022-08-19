# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n

    numbers = [0, 1]
    n = n % 60 # the Pisano period for Fi mod 10 is 60.

    if n == 0:
        return 0

    for i in range(2, n + 3):
        numbers.append((numbers[i - 1] + numbers[i - 2]) % 60)

    return (numbers.pop() - 1) % 10

def fiboniacci_sum(n):
    return get_fibonacci_last_digit(n)

if __name__ == '__main__':
    input = input()
    n = int(input)
    print(fiboniacci_sum(n))
