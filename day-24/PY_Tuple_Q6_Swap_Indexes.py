def swap_indexes(tup, i, j):
    lst = list(tup)            # convert tuple → list
    lst[i], lst[j] = lst[j], lst[i]  # swap
    return tuple(lst)          # convert back → tuple

tup = (10, 20, 30, 40, 50)

new_tup = swap_indexes(tup, 1, 3)

print(f"Original tuple : {tup}")
print(f"Swapped tuple  : {new_tup}")
