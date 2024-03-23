def k(n):
    lst_mines = [1] * n * 100
    lst_mines[3] = 0
    if n == 1 or n == 2:
        print(n * lst_mines[n - 1])
    elif n == 3:
        print(4 * lst_mines[2])
    else:
        lst = [1, 2, 4]
        for i in range(3, n):
            # lst.append(sum([lst_mines[i] * lst[i] for i in range(-1, -4, -1)]))
            lst.append((lst[i - 1]
                       + lst[i - 2]
                       + lst[i - 3]) * lst_mines[i])
        print(lst[-1])


k(3)
k(4)
k(5)
