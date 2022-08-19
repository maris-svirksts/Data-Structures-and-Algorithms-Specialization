# Uses python3

# https://www.geeksforgeeks.org/last-digit-of-sum-of-numbers-in-the-given-range-in-the-fibonacci-series/

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def get_fibonacci_sum(n):
    if n < 1:
        return 0

    numbers = [0, 1]
    n = n % 60 # the Pisano period for Fi mod 10 is 60.

    for i in range(2, n + 3):
        numbers.append((numbers[i - 1] + numbers[i - 2]) % 60)

    return (numbers.pop() - 1)

if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    print((get_fibonacci_sum(to) - get_fibonacci_sum(from_ - 1)) % 10)
