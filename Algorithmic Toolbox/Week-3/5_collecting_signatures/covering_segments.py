# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda tup: tup.start)
    #write your code here

    points.append(segments[0].end)
    for s in segments:
        if points[-1] < s.start:
            points.append(s.end)
        elif points[-1] > s.end:
            points.pop()
            points.append(s.end)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
