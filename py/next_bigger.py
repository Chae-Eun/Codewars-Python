###########################MY SOLUTION###############################
def next_bigger(n):
    if len(str(n)) <= 1:
        return -1

    count = 2
    nstr = str(n)
    nlist = list(nstr)
    nlen = len(nstr)

    while(True):
        if int(nstr[-1]) > int(nstr[-2]):
            return int(nstr[:-2] + nstr[-1] + nstr[-2])
        elif nlen > count:
            for i in range(1, count+1):
                nlist = nlist[:-count] + sorted(nlist[-count:])
                if nlist[-(count+1)] < nlist[-i]:
                    if (nlist[-(count+1)] >= nlist[-(i+1)]) or (i == count):
                        nlist.append(nlist[-(count+1)])
                        nlist[-(count+2)] = nlist[-(i+1)]
                        del(nlist[-(i+1)])
                        return int("".join(nlist[:-count] + sorted(nlist[-count:])))
                    else:
                        continue
                else:
                    count += 1
                    break
        else:
            return -1

#########################BEST SOLUTION###############################
import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
#####################################################################