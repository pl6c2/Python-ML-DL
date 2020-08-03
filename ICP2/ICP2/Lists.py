lbs = []
number = int(input("enter the size of a list"))
for x in range(number):
    e = input("enter an element")  # reading list
    lbs.append(int(e))

print(lbs)

# kgs = []     # second list

#
# for x in lbs:
#     kgs.append(round(x * 0.45359, 2))   # converting into kgs

kgs = [round(lb * 0.45359, 2) for lb in lbs]  # list comprehensions

print(kgs)



