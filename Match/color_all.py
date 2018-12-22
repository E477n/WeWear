def allcolor(b):
    import traceback
    import random

    choice1 = list()
    choice2 = list()
    choice3 = list()
    choice4 = list()
    choice5 = list()
    choice6 = list()
    choice7 = list()
    choice8 = list()
    choice = list()
    try:
        if b[0]:
            for i in b[0]:
                if i:
                    choice1.append(i[random.randint(0, len(i)-1)][0])
                    choice2.append(i[random.randint(0, len(i)-1)][0])
        if b[1]:
            for i in b[1]:
                if i:
                    choice3.append(i[random.randint(0, len(i)-1)][0])
                    choice4.append(i[random.randint(0, len(i)-1)][0])
        if b[2]:
            for i in b[2]:
                if i:
                    choice5.append(i[random.randint(0, len(i)-1)][0])
                    choice6.append(i[random.randint(0, len(i)-1)][0])
        if b[3]:
            for i in b[3]:
                if i:
                    choice7.append(i[random.randint(0, len(i)-1)][0])
                    choice8.append(i[random.randint(0, len(i)-1)][0])

        choice.append(choice1)
        choice.append(choice2)
        choice.append(choice3)
        choice.append(choice4)
        choice.append(choice5)
        choice.append(choice6)
        choice.append(choice7)
        choice.append(choice8)
    except:
        traceback.print_exc()

    return choice



