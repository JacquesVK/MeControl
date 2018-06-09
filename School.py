def school(childrens, teacher):
    peremennay = "Сейчас бы пойти"
    print(peremennay)

    def add():
        nonlocal peremennay
        peremennay= peremennay + " гулять в +100"

    add()
    print('В итоге я получил - ',peremennay)

    while teacher < childrens:
        childrens = childrens // 3
        if childrens == 200:
            childrens = childrens + 150
            print("Но их {} и они не помещаются в класс!!".format(childrens))
        else:
            print("Все же их: ", childrens)
    else:
        print("Учителя победили!!!")

school(600, 55)
