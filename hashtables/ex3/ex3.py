def intersection(arrays):
    results = []
    lookup = dict()

    # Enter outer array
    for array in arrays:
        # Loop through inner array
        for num in array:
            # If value is not in table
            if num not in lookup:
                # add to table
                lookup[num] = 1
            # If value is in table increase value by 1
            else:
                lookup[num] = lookup[num] + 1
            # If value is in every array add to results
            if lookup[num] >= len(arrays):
                results.append(num)
            

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
