def max_pairwise_product_original(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product(numbers):
    first_value  = numbers[0]
    second_value = numbers[1]

    for i in numbers[2:]:
        if i > first_value and first_value >= second_value:
            second_value = i
        elif i > first_value:
            first_value = i
        elif i > second_value:
            second_value = i
    
    return first_value * second_value

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
