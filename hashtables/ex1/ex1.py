#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        weight = weights[i]
        weight_two = limit - weight
        found_weight = hash_table_retrieve(ht, weight_two)
        if found_weight:
            if i < found_weight:
                return (found_weight, i)
            else:
                return (i, found_weight)
        #hash_table_insert(weight, )



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
