class Toy():
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def sing(self, song):
        print(song)


class BearToy(Toy):
    def __init__(self, size, color, mat):
        super().__init__(size, color)
        # super(Toy, self).__init__(size, color)
        self.mat = mat

    def run(self):
        print("I can run")


if __name__ == '__main__':
    tidy = BearToy('small', 'yellow', 'leg')
    tidy.sing("shangshandalaohu")
    tidy.run()
    print(tidy.size, tidy.color, tidy.mat)
