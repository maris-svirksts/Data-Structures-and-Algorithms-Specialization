# Uses python3

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def calc_fib(n):
    if (n <= 1):
        return n

    numbers = [0, 1]

    for i in range(2, n + 1):
        numbers.append(numbers[i - 1] + numbers[i - 2])

    return numbers.pop()

# Pisaro code translated to Python from https://mathoverflow.net/questions/144308/calculating-pisano-periods-for-any-integer conversation.
def get_pisano_period(m):
    i = 0
    a = 0
    b = 1
    c = 1

    limit = 1

    while i < limit:
        c  = (a + b) % m
        a  = b
        b  = c

        if a == 0 and b == 1:
            return i + 1

        limit = limit + 1
        i    += 1

def get_fibonacci_huge(n, m):
    pisano   = get_pisano_period(m)
    reminder = n % pisano
    
    return calc_fib(reminder) % m

if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
