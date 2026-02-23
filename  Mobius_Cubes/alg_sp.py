# sp_algorithm.py

def get_bit(x, i):
    return (x >> i) & 1


def flip_bit(x, i):
    return x ^ (1 << i)


# ===============================
# Algoritmo SP
# ===============================

def SP(s, t, n):

    w = s ^ t
    S = set()
    i = 0

    while i < n:
        if get_bit(w, i) == 0:
            i += 1
        else:
            if i == n - 1:
                S.add(i)
                i += 1
            else:
                if get_bit(w, i + 1) == 0:
                    S.add(i)
                    i += 2
                else:
                    S.add(i)
                    w = flip_bit(w, i)
                    i += 2

    return SP0(s, S)


def SP0(s, S):

    path = [s]
    current = s

    for i in sorted(S):
        current = flip_bit(current, i)
        path.append(current)

    return path