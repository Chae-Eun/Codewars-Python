###########################MY SOLUTION###############################
def duplicate_encode(word):
    result = ''
    for i in range(len(word)):
        if word.lower().count(word[i].lower()) > 1:
            result += ')'
        else:
            result += '('
    return result

#########################BEST SOLUTION###############################
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
#####################################################################