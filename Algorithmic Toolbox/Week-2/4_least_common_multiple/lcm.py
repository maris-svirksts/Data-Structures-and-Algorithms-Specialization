# Uses python3

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    if b == 0:
        return int(a)
    
    return gcd(b, a % b)

def lcm(a, b):
    return int(abs(a) * ( abs(b) / gcd(a, b) ))

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))

