

back = [1, 2, 3, 4, 5]

print(back[4])
print(back[3])
print(back[2])
print(back[1])
print(back[0])


def iterate(lst):
    for i in range(len(lst), 0, -1):
        print(i)


iterate(back)
