def distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0 if s[-1] == t[-1] else 1
        d1 = distance(s[:-1], t) + 1
        d2 = distance(s, t[:-1]) + 1
        d3 = distance(s[:-1], t[:-1]) + cost
        return min(d1, d2, d3)


print(distance("prototype", "probleming"))
