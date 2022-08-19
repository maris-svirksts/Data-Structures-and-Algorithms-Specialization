# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    numbers = [0, 1]

    for i in range(2, n + 1):
        numbers.append(numbers[i - 1] + numbers[i - 2])

    return numbers.pop()

n = int(input())
print(calc_fib(n))
