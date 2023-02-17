import math


def Min_edge(R, U):
    check_value = (math.inf, -1, -1)
    for v in U:
        find_value = min(R, key=lambda x: x[0] if (x[1] == v or x[2] == v) and (x[1] not in U or x[2] not in U) else math.inf)
        if math.inf != find_value[0]:
            check_value = find_value

    return check_value


R = [(math.inf, -1, -1), (15, 1, 2), (14, 1, 5), (23, 1, 4), (19, 2, 3), (16, 2, 4), (15, 2, 5), (14, 3, 5), (26, 3, 6),
     (25, 4, 5), (23, 4, 7), (20, 4, 8), (24, 5, 6), (27, 5, 8), (18, 5, 9), (14, 7, 8), (18, 8, 9)]

N = 9
U = {1}
T = []

while len(U) < N:
    r = Min_edge(R, U)
    if r[0] == math.inf:
        break
    T.append(r)
    U.add(r[1])
    U.add(r[2])

print(T)
