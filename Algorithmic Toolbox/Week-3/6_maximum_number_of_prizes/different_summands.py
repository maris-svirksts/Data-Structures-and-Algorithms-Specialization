# Uses python3
# math from https://stackoverflow.com/questions/54608210/different-summands-problem-greedy-alogrithm
import sys
from math import floor, sqrt

def optimal_summands(n):
    summands = []
    #write your code here
    summands_count = floor((sqrt(8 * n + 1)-1) / 2)
    summands       = [i for i in range(1, summands_count)]
    last_summand   = int(n - summands_count * (summands_count - 1) / 2)

    summands.append(last_summand)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
