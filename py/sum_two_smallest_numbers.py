###########################MY SOLUTION###############################
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]

#########################BEST SOLUTION###############################
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
#####################################################################