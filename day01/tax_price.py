while True:
    l = int(input("Please input the longth: "))
    if l <= 3:
        price = 13
    elif l <= 10:
        price = 13 + (l-3)*2.4
    else:
        price = 13 + (10-3)*2.4 + (l-10)*3.6
    print("You need pay ${}.".format(price))
