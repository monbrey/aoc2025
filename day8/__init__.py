import math
from utils.io import read_input_for


def read_input(strip: bool = True) -> str:
    """Return the contents of this module's `input.txt`."""
    return read_input_for(__file__, strip=strip)

def euc_dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def a():
    """Part a for day4."""
    data = read_input()
    if not data:
        return "input.txt not found or empty"
    
    junctions = [tuple(int(x) for x in point.split(",")) for point in data.splitlines()]
    circuits = [[j] for j in junctions]
    # calculating all distances and sorting probably isn't most efficient
    # j > i ensures we don't double-calculate reverse relationships
    dists = sorted([(p,q,euc_dist(p,q)) for i,p in enumerate(junctions) for j,q in enumerate(junctions) if j > i], key=lambda x: x[2])

    # Instructions say to make 1000 connections
    for d in dists[:1000]:
        c1 = [c for c in circuits if d[0] in c][0]
        c2 = [c for c in circuits if d[1] in c][0]
        if(c1 == c2):
            # Ignore if in same circuit
            continue
        else:
            circuits.remove(c1)
            circuits.remove(c2)
            circuits.append(c1 + c2)

    circuits = sorted(circuits, key=len, reverse=True)
    return math.prod(len(c) for c in circuits[:3])


def b():
    """Part b for day4."""
    data = read_input()
    if not data:
        return "input.txt not found or empty"


    junctions = [tuple(int(x) for x in point.split(",")) for point in data.splitlines()]
    circuits = [[j] for j in junctions]
    dists = sorted([(p,q,euc_dist(p,q)) for i,p in enumerate(junctions) for j,q in enumerate(junctions) if j > i], key=lambda x: x[2])

    for d in dists:
        c1 = [c for c in circuits if d[0] in c][0]
        c2 = [c for c in circuits if d[1] in c][0]
        if(c1 == c2):
            # print("Both points already in same circuit, skipping")
            continue
        else:
            # print("Merging circuits",c1,"and",c2)
            circuits.remove(c1)
            circuits.remove(c2)
            circuits.append(c1 + c2)
        
        if len(circuits) == 1:
            return d[0][0] * d[1][0]
