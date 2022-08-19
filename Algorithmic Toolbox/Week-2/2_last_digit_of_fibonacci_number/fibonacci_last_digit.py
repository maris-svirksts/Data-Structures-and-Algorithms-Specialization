# Uses python3
def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n

    numbers = [0, 1]

    for i in range(2, n + 1):
        numbers.append((numbers[i - 1] + numbers[i - 2]) % 10)

    return numbers.pop()

if __name__ == '__main__':
    input = input()
    n = int(input)
    print(get_fibonacci_last_digit(n))
