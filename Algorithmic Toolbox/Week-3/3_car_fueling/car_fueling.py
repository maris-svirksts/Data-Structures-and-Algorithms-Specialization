# python3

def compute_min_refills(location, stops, milage, distance, counter):
    if location + milage >= distance:
        return counter
    if not stops or (stops[0] - location) > milage:
        return -1

    last_stop = location
    while stops and (stops[0] - location) <= milage:
        last_stop = stops[0]
        stops     = stops[1:]
    
    return compute_min_refills(last_stop, stops, milage, distance, counter + 1)

if __name__ == '__main__':
    distance = int(input())
    milage   = int(input())
    _        = int(input())
    stops    = list(map(int, input().split()))

    print(compute_min_refills(0, stops, milage, distance, 0))
