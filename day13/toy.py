class Vender():
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

    def get_phone(self):
        return self.phone

    def update_phone(self, phone):
        self.phone = phone


class Toy():
    def __init__(self, size, color, phone, email):
        self.size = size
        self.color = color
        self.vender = Vender(phone, email)

    def sing(self, song):
        print(song)


if __name__ == '__main__':
    tidy = Toy('small', 'yellow', '15618553602', 'xxx@foxmail.com')
    tidy.sing("shangshandalaohu")
    print(tidy.vender.get_phone())
    tidy.vender.update_phone('17028428738')
    print(tidy.vender.get_phone())