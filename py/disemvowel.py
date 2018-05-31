###########################MY SOLUTION###############################
import re
def disemvowel(string):
    string = re.sub('[AIEOUaieou]', "", string)
    return string

#########################BEST SOLUTION###############################
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
#####################################################################