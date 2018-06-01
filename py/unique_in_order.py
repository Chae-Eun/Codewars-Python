###########################MY SOLUTION###############################
def unique_in_order(iterable):
    order = list(iterable)
    count = 0

    while(count < len(order)-1):
        if order[count] == order[count+1]:
            del(order[count])
            count = 0
        else:
            count += 1

    return order

#########################BEST SOLUTION###############################
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
#####################################################################