###########################MY SOLUTION###############################
def validBraces(string):
    braces = ['()', '{}', '[]']

    while(True):
        for i in range(len(string)):
            if "".join(string[i:i+2]) in braces:
                string = string[:i] + string[i+2:]
                continue

        if len(string) == 0:
            break
        else:
            if braces[0] in string or braces[1] in string or braces[2] in string:
                pass
            else:
                return False

    return True

#########################BEST SOLUTION###############################
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0

def validBraces(s):
    while '{}' in s or '()' in s or '[]' in s:
        s=s.replace('{}','')
        s=s.replace('[]','')
        s=s.replace('()','')
    return s==''
#####################################################################