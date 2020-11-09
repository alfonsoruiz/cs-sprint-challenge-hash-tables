#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    lookup = {}
    route = []

    for flight in tickets:
        lookup[flight.source] = flight.destination

    route.append(lookup['NONE'])

    for i in range(1, length):
        # lookup[route[i - 1]] returns the value of the key in lookup
        route.append(lookup[route[i - 1]])

    return route
