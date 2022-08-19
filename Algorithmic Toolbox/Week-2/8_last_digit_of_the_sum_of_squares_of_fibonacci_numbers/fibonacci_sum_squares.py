# Uses python3

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def get_fibonacci_sum(n):
    if n < 1:
        return (0, 0)

    numbers = [0, 1]
    n = n % 60 # the Pisano period for Fi mod 10 is 60.
 
    for i in range(2, n + 1):
        numbers.append((numbers[i - 1] + numbers[i - 2]) % 60)

    return ((numbers.pop(), numbers.pop()))

if __name__ == '__main__':
    n = int(input())

    a, b = get_fibonacci_sum(n + 1)
 
    print((a * b) % 10)
