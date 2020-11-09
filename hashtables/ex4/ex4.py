def has_negatives(a):
    lookup = set()
    result = []

    for n in a:
        if n < 0:
            n = abs(n)

        if n in lookup:
            result.append(n)
        else:
            lookup.add(n)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
