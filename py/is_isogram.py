###########################MY SOLUTION###############################
def is_isogram(string):
    isogram = []

    for i in range(len(string)):
        if string[i].lower() in isogram:
            return False
        else:
            isogram.append(string[i].lower())

    return True

#########################BEST SOLUTION###############################
def is_isogram(string):
    return len(string) == len(set(string.lower()))
#####################################################################