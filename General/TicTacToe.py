
# for row in range(5):
#     if row % 2 == 0:
#         print(' | | ')
#     else:
#         print('-----')


for row in range(5):
    if row % 2 == 0:
        for x in range(2):
            print(' ', end='')
            print('|', end='')
    else:
        print('-----', end='')
    print('')