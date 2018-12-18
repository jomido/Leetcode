
from sys import float_info

E = float_info.epsilon


meetings = {
    (
        (1, 3), (3, 5), (5, 7)
    ): 1,
    (
        (1, 3), (2, 4), (3, 5)
    ): 2,
    (
        (1, 3), (1, 4), (1, 2)
    ): 3
}


def prep(times):

    _times = []

    for time in times:
        _times.append(tuple(range(time[0], time[1])) + (time[1] - 0.1,))

    return _times


def collide(times):

    from itertools import combinations

    colls = 0

    for c in combinations(times, 2):

        d = set(c[0]).difference(set(c[1]))
        if d != set(c[0]):
            colls += 1

    return colls


def required_rooms(meetings):

    required = tuple()

    for times in meetings.keys():

        times = prep(times)
        collisions = collide(times)
        required += (max(collisions, 1),)

    return required


if __name__ == "__main__":

    expected = tuple(meetings.values())  # (0, 2, 3)

    assert expected == required_rooms(meetings)

    print("dope.")
