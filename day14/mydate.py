class MyDate():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def create_date(cls, string_date):
        year, month, day = map(int, string_date.split('-'))
        date = cls(year, month, day)
        return date

    @staticmethod
    def is_date_valid(string_date):
        year, month, day = map(int, string_date.split('-'))
        return year < 4000 and 0 < month < 13 and 0 < day < 32


if __name__ == '__main__':
    d1 = MyDate(2018, 3, 24)
    print(d1.year, d1.month, d1.day)
    d2 = MyDate.create_date('2029-03-01')
    print(d2.year, d2.month, d2.day)
    print(MyDate.is_date_valid('2019-38-29'))
