import matplotlib.pyplot as plt
from collections import defaultdict
import itertools

# =========================
# Parte 1 — Cálculo dos λ
# =========================

def w(i, j, n, r, a):
    if j != a:
        return 2 ** j
    else:
        if n % 2 == 0 and r % 2 == 1:
            return 2 ** (n - r)
        else:
            return 2 ** (n - r - 1)


def calculate_w1(n, r):
    g = 0
    if (n % 2 == 0 and r % 2 == 0) or (n % 2 == 0 and r % 2 == 1):
        g = 1

    if (n % 2 == 0 and r % 2 == 0) or (n % 2 == 1 and r % 2 == 0):
        h = n - r - 4
    elif n % 2 == 0 and r % 2 == 1:
        h = n - r - 1
    else:
        h = n - r - 3

    w1 = []
    for s in range(g, h + 1, 2):
        w1.append(2 ** (s + 1))

    return w1


def calculate_w2(n, r):
    if n % 2 == 0 and r % 2 == 0:
        m = n - r
    elif (n % 2 == 0 and r % 2 == 1) or (n % 2 == 1 and r % 2 == 1):
        m = n - r + 1
    else:
        m = n - r - 2

    w2 = []
    for t in range(m, n, 2):
        w2.append(2 ** (t + 1))

    return w2


def compute_lambda_set(n, r):
    if r % 2 == 0:
        k = 2 ** (n - r - 1)
    else:
        k = 2 ** (n - r)

    l = None
    if n % 2 == r % 2:
        l = 2 ** (n - r - 1)

    w1 = calculate_w1(n, r)
    w2 = calculate_w2(n, r)

    termssum = [k] + w1 + w2

    if n % 2 == 0:
        termssum.append(1)

    if l is not None:
        termssum.append(l)

    return termssum


# =========================
# Parte 2 — Estruturas
# =========================

class Fiber:
    def __init__(self, lambda_max=32):
        self.lambda_total = 0
        self.assigned_cycles = []
        self.lambda_used_per_edge = defaultdict(
            lambda: set(range(1, lambda_max + 1))
        )


def is_disjoint(cycle, assigned_cycles):
    cycle_set = set(cycle)
    for c, _ in assigned_cycles:
        if cycle_set.intersection(set(c)):
            return False
    return True


def checkFoH(cycle, lamb, lambda_total, lambda_vertex,
             lambda_used_per_edge,
             lambda_max_fiber=32,
             Pmax_vertex=32):

    if lambda_total > lambda_max_fiber:
        return False

    for edge in cycle_edges(cycle):
        if lamb not in lambda_used_per_edge[edge]:
            return False

    for v in cycle:
        if lambda_vertex[v] + 1 > Pmax_vertex:
            return False

    return True


def cycle_edges(cycle):
    return [(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1)]


# =========================
# Parte 3 — Geração simplificada de ciclos
# =========================

def generate_simple_cycles(n):
    vertices = list(range(2 ** n))
    cycles = []

    for u in vertices:
        for i in range(n - 1):
            v1 = u
            v2 = u ^ (1 << i)
            v3 = v2 ^ (1 << (i + 1))
            v4 = u ^ (1 << (i + 1))
            cycle = (v1, v2, v3, v4, v1)
            cycles.append(cycle)

    return cycles


# =========================
# Parte 4 — Algoritmo Principal
# =========================

def lambda_assignment(n, r):
    lambda_values = compute_lambda_set(n, r)
    cycles = generate_simple_cycles(n)

    fibers = [Fiber()]
    lambda_vertex = defaultdict(int)

    for cycle in cycles:
        assigned = False

        for fiber in fibers:
            for lamb in lambda_values:
                if is_disjoint(cycle, fiber.assigned_cycles) and \
                   checkFoH(cycle, lamb, fiber.lambda_total,
                            lambda_vertex,
                            fiber.lambda_used_per_edge):

                    for edge in cycle_edges(cycle):
                        fiber.lambda_used_per_edge[edge].discard(lamb)

                    for v in cycle:
                        lambda_vertex[v] += 1

                    fiber.lambda_total += 1
                    fiber.assigned_cycles.append((cycle, lamb))
                    assigned = True
                    break

            if assigned:
                break

        if not assigned:
            new_fiber = Fiber()
            fibers.append(new_fiber)

    return fibers


# =========================
# Parte 5 — Plot
# =========================

def plot_result(fibers):
    lambda_counts = [fiber.lambda_total for fiber in fibers]

    plt.figure()
    plt.bar(range(len(lambda_counts)), lambda_counts)
    plt.xlabel("Fiber Index")
    plt.ylabel("Total λ Assigned")
    plt.title("λ Assignment per Fiber")
    plt.show()


# =========================
# Execução
# =========================

if __name__ == "__main__":
    n = 4
    r = 2

    fibers = lambda_assignment(n, r)
    plot_result(fibers)