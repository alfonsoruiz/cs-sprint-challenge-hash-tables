#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    lookup = dict()

    # Loop through tickets
    for ticket in tickets:
        # Add key as source and value as destination to table
        lookup[ticket.source] = ticket.destination

    # Build route with first location
    route = [lookup["NONE"]]

    # Get next location based on previous location 
    for i in range(1,length):
        # Add to route
        route.append(lookup[route[i - 1]])

    return route
