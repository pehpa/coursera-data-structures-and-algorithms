from sys import stdin
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    # sort segments by start
    segments = sorted(segments, key=attrgetter('start'))

    points = []

    while len(segments) > 0:
        candidate_segments = []
        min_p = 1000000001
        max_p = -1

        # collect all candidate segments
        for s in segments:
            if len(candidate_segments) == 0:
                candidate_segments.append(s)
                min_p = s.start
                max_p = s.end
            elif (s.start >= min_p and s.start <= max_p) or (s.end >= min_p and s.end <= max_p):
                candidate_segments.append(s)
                if s.start > min_p:
                    min_p = s.start
                if s.end < max_p:
                    max_p = s.end
            else:
                break
        points.append(min_p)

        # remove candidate segments from sorted segment list
        segments = segments[len(candidate_segments):]

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())

    # data = [1, 3, 2, 5, 3, 6]
    # data = [4, 7, 1, 3, 2, 5, 5, 6]
    # data = [1, 8, 2, 15, 7, 24]
    # data = [1, 6, 2, 5, 3, 15, 4, 19, 7, 16, 15, 20, 17, 21]
    # data = [2, 18, 5, 10, 2, 6, 5, 7, 21, 23, 13, 15, 9, 13, 9, 21, 4, 10, 8, 11, 17, 20, 8, 17]
    # data = [1, 2, 5, 5, 4, 6, 4, 7, 0, 4]

    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))

    points = optimal_points(segments)

    print(len(points))
    print(*points)
