while True:
    g_s = input("Please input the grade points: ")
    g = int(g_s)
    if g >= 0 and g < 60:
        print("Your point is {}, your score are BAD.".format(g))
    elif g >= 60 and g < 80:
        print("Your point is {}, your score are MEDIUM.".format(g))
    elif g >= 80 and g < 90:
        print("Your point is {}, your score are GOOD.".format(g))
    elif g >= 90 and g <= 100:
        print("Your point is {}, your score are GREAT.".format(g))
    else:
        print("Your point is illegal. ")
