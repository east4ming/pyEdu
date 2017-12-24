while True:
    g_s = input("Please input the grade points: ")
    g = int(g_s)
    if g < 0 or g > 100:
        print("Your point is illegal. ")
    else:
        if g < 60:
            print("Your point is {}, your score are BAD.".format(g))
        elif 60 <= g < 80:
            print("Your point is {}, your score are MEDIUM.".format(g))
        elif 80 <= g < 90:
            print("Your point is {}, your score are GOOD.".format(g))
        else:
            print("Your point is {}, your score are GREAT.".format(g))
