#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    counter = 0

    next_ticket = hash_table_retrieve(hashtable, "NONE")
    route[counter] = next_ticket
    counter += 1
    length -= 1

    while length != 0:
        ticket_after = hash_table_retrieve(hashtable, next_ticket)
        route[counter] = ticket_after
        next_ticket = route[counter]
        counter += 1
        length -= 1

    return route[:-1]
