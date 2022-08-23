# Uses python3

def get_optimal_value(capacity, things_to_steal):
    value           = 0.
    things_to_steal = sorted(things_to_steal, key=lambda tup: tup[0] / tup[1], reverse=True)

    for i in things_to_steal:
        if capacity == 0:
            return value
        elif i[1] <= capacity:
            value    += i[0]
            capacity -= i[1]
        else:
            value   += (i[0] * (capacity / i[1]))
            capacity = 0
    
    return value


if __name__ == "__main__":
    things_to_steal = []
    n, capacity     = list(map(int, input().split()))

    for _ in range(n):
        value, weight   = list(map(int, input().split()))
        things_to_steal.append((value, weight))

    opt_value = get_optimal_value(capacity, things_to_steal)
    print("{:.4f}".format(opt_value))
