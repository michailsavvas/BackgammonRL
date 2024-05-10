from collections import Counter

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as Counters, return
    their dot product.
    """
    dot=0
    dot=dot + sum( [ v1[index]*v2[index] for index in set(v1) & set(v2) ] )
    return dot

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    """
    for index in set(v2):
        v1[index]+=scale*v2[index]
    return v1

def normalizeWeights(v):
    total = 0
    counter = 0
    for index in v:
        if v[index] != 0:
            counter += 1
        total += v[index]
    w = Counter({})
    for index in v:
        w[index] = (v[index] / total) * counter
    return w