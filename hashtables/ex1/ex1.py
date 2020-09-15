def get_indices_of_item_weights(weights, length, limit):
    lookup = dict()

    # Loop through weights list
    for i in range(length):
        if weights[i] in lookup:
            # check table for index of item
            index = lookup[weights[i]]
            # return loop index and lookup index as tuple
            return (i, index)
        # check table for limit match
        lookup[limit - weights[i]] = i

    # If pair doesn't exist return None
    return None