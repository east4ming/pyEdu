weight = float(input("Please input your body weight (KG): "))
height = float(input("Please input your body height (M): "))
fat_level = weight/(height**2)
if fat_level < 18:
    print("{} You are too thin.".format(fat_level))
elif fat_level < 24:
    print("{} Your body weight is normal. Congratulations!".format(fat_level))
else:
    print("{} You are too fat!".format(fat_level))
