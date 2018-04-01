import re
import collections


class CounterLog():
    def __init__(self, fname, patt):
        self.fname = fname
        self.cpatt = re.compile(patt)
        self.counter = collections.Counter()

    def count(self):
        with open(self.fname) as fobj:
            for line in fobj:
                m = self.cpatt.search(line)
                if m:
                    self.counter.update([m.group()])
        return self.counter


if __name__ == '__main__':
    fname = 'access_log.txt'
    ip_patt = r"^(\d+\.){3}\d+"
    a = CounterLog(fname, ip_patt)
    print(a.count())
    br_patt = r'Firefox|MSIE|Chrome'
    b = CounterLog(fname, br_patt)
    print(b.count())