

def hour_summary(l):
    d = dict()
    for key, size in l:
        k = key[:32]
        if k in d:
            d[k] += size
        else:
            d[k] = size
    return d
