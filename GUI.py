picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
# line 9_12 allows to have the tree 3 times
i = 0
while i < 3:
    i += 1

    for image in picture:
        for pixel in image:
            if pixel == 1:
                print('*', end='')
            else:
                print(' ', end='')
        #  need a new line afer running the nexted loop
        print('')


