def pokaz():
    b = []
    e = ''
    v = 0
    with open("Info.txt", encoding='utf-8') as f:
        a = f.readlines()
        j = 0
        for i in a:
            b.append(i.strip().split(', '))
            c = int(b[j][1])

            if c >= 1997:
                e += f'{i} '
                v += 1
            j += 1

        print(v)
        print(e)
        h = open('save.txt', 'w', encoding='utf-8')
        h.write(e)
        h.close()

pokaz()
