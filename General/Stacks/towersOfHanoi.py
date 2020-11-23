def hanoiTowers(n, start, end):
    if n == 1:
        print(start, ' -> ', end)
    else:
        other = 6 - (start + end)
        hanoiTowers(n - 1, start, other)
        print(start, ' -> ', end)
        hanoiTowers(n - 1, other, end)
        

hanoiTowers(3, 1, 3)