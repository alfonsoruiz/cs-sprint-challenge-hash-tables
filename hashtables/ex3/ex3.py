def intersection(arrays):
    lookup = dict()
    result = []

    for arr in arrays:
        for n in arr:
            if n in lookup:
                lookup[n] += 1
            else:
                lookup[n] = 1

    for key, value in lookup.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
