###########################MY SOLUTION###############################
def find_nb(m):
    n = 0

    while(True):
        n = n + 1
        m = m - (n*n*n)

        if m == 0:
            return n
        elif m < 0:
            return -1

#########################BEST SOLUTION###############################
def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1
#####################################################################