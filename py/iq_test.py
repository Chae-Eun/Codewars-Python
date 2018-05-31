###########################MY SOLUTION###############################
def iq_test(numbers):
    count = 0
    num = numbers.split()

    for i in range(len(num)):
        count += int(num[i])%2

    if count == 1 : #odd
        for j in range(len(num)):
            if int(num[j])%2 == 1:
                return j+1
    else: #even
        for j in range(len(num)):
            if int(num[j])%2 != 1:
                return j+1

#########################BEST SOLUTION###############################
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
#####################################################################