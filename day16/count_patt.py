import re
import collections


def count_patt(fname, patt):
    counter = collections.Counter()
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                counter.update([m.group()])
    return counter


if __name__ == '__main__':
    fname = 'access_log.txt'
    ip_patt = r"^(\d+\.){3}\d+"
    a = count_patt(fname, ip_patt)
    print(a)
    br_patt = r'Firefox|MSIE|Chrome'
    b = count_patt(fname, br_patt)
    print(b)