def dessine_un_sapin():
    n = 9
    i = 1
    while 1 <= n:
        print(" "*n + "^"*i)
        i+=2
        n -=1

dessine_un_sapin()