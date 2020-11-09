def get_indices_of_item_weights(weights, length, limit):
    lookup = {}

    for i in range(length):
        #  If weight value in is a key in lookup
        if weights[i] in lookup:
            # Get and set value from lookup at specified key
            index = lookup[weights[i]]
            return (i, index)

        # Key in lookup = limit - index at weights i in list and value
        lookup[limit - weights[i]] = i

    return None
