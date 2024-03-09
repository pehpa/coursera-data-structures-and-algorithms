from sys import stdin


def get_next_stop(max_reach, curr_mile, stops):
    next_stop = -1
    for stop in stops:
        if stop > curr_mile and stop <= max_reach:
            next_stop = stop
    return next_stop


def min_refills(distance, tank, stops):
    total_stops = 0
    curr_mile = 0
    max_reach = curr_mile + tank

    while max_reach < distance:
        # print('curr mile before = {:>4}, max reach before = {:>4}, '.format(curr_mile, max_reach), end='')

        # get next stop distance and set current mile
        curr_mile = get_next_stop(max_reach, curr_mile, stops)
        # print('curr mile after = {:>4}'.format(curr_mile), end='')

        # if no next stop could be found within reach, break and state that destination is not reachable
        if curr_mile == -1:
            total_stops = -1
            # print(" (destination cannot be reached)")
            break
        # if next stop could be found, one more stop was done and current mile is stop mile
        else:
            total_stops = total_stops + 1
            max_reach = curr_mile + tank
            # print(', max reach after = {:>4}'.format(max_reach))

    return total_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())

    # d = 950
    # m = 400
    # stops = [200, 375, 550, 750]

    # d = 10
    # m = 3
    # stops = [1, 2, 5, 9]

    # d = 200
    # m = 250
    # stops = [100, 150]

    # print(d, m, stops)

    print(min_refills(d, m, stops))
