def color_match(a, b):
    scheme = list()
    main0 = list() # 黑白两色
    main1 = list() # 高饱和度配色
    main2 = list() # 高饱和度撞色
    main3 = list() # 非高饱和度配色
    hmin = a[0] - 20
    hmax = a[0] + 20

    # 0主题色 黑白大类
    if a[2]>=0 and a[2]<=0.1:
        #外套
        coat = list()
        for each in b[0]:
            if each[3]>=0 and each[3]<=0.1:
                coat.append(each)
        main0.append(coat)

        # 上装
        tops = list()
        for each in b[1]:
            if each[3] >= 0 and each[3] <= 0.1:
                tops.append(each)
        main0.append(tops)

        # 内衬
        lining = []
        for each in b[2]:
            if each[3] >= 0 and each[3] <= 0.1:
                lining.append(each)
        main0.append(lining)

        # 内搭
        inside = []
        for each in b[3]:
            if each[3] >= 0 and each[3] <= 0.1:
                inside.append(each)
        main0.append(inside)

        # 连体套装
        piece_suit = []
        for each in b[4]:
            if each[3] >= 0 and each[3] <= 0.1:
                piece_suit.append(each)
        main0.append(piece_suit)

        # 连衣套装
        dress_suit = []
        for each in b[5]:
            if each[3] >= 0 and each[3] <= 0.1:
                dress_suit.append(each)
        main0.append(dress_suit)

        # 西装套装
        suit = []
        for each in b[6]:
            if each[3] >= 0 and each[3] <= 0.1:
                suit.append(each)
        main0.append(suit)

        # 裤装
        trousers = []
        for each in b[7]:
            if each[3] >= 0 and each[3] <= 0.1:
                trousers.append(each)
        main0.append(trousers)

        # 裙装
        skirt = []
        for each in b[8]:
            if each[3] >= 0 and each[3] <= 0.1:
                skirt.append(each)
        main0.append(skirt)

        # 鞋子
        shoes = []
        for each in b[9]:
            if each[3] >= 0 and each[3] <= 0.1:
                shoes.append(each)
        main0.append(shoes)

        # 配饰
        accessories = []
        for each in b[10]:
            if each[3] >= 0 and each[3] <= 0.1:
                accessories.append(each)
        main0.append(accessories)

    # 1主题色 高饱和度配色 + 2主题色 高饱和度撞色
    if a[2]>=0.35 and a[2]<=0.65 and a[1]>0.5:
        # 外套
        coat1 = list()
        coat2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[0]:
                if each[1] in (hmin, hmax):
                    coat1.append(each)
                if each[1]>=140 and each[1]<=280:
                    coat2.append(each)
        else:
            for each in b[0]:
                if each[1] in (hmin, hmax):
                    coat1.append(each)
                if float(each[1])<140 or float(each[1])>280:
                    coat2.append(each)
        main1.append(coat1)
        main2.append(coat2)

        # 上装
        tops1 = list()
        tops2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[1]:
                if each[1] in (hmin, hmax):
                    tops1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    tops2.append(each)
        else:
            for each in b[1]:
                if each[1] in (hmin, hmax):
                    tops1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    tops2.append(each)
        main1.append(tops1)
        main2.append(tops2)

        # 内衬
        lining1 = list()
        lining2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[2]:
                if each[1] in (hmin, hmax):
                    lining1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    lining2.append(each)
        else:
            for each in b[2]:
                if each[1] in (hmin, hmax):
                    lining1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    lining2.append(each)
        main1.append(lining1)
        main2.append(lining2)

        # 内搭
        inside1 = list()
        inside2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[3]:
                if each[1] in (hmin, hmax):
                    inside1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    inside2.append(each)
        else:
            for each in b[3]:
                if each[1] in (hmin, hmax):
                    inside1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    inside2.append(each)
        main1.append(inside1)
        main2.append(inside2)

        # 连体套装
        piece_suit1 = list()
        piece_suit2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[4]:
                if each[1] in (hmin, hmax):
                    piece_suit1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    piece_suit2.append(each)
        else:
            for each in b[4]:
                if each[1] in (hmin, hmax):
                    piece_suit1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    piece_suit2.append(each)
        main1.append(piece_suit1)
        main2.append(piece_suit2)

        # 连衣套装
        dress_suit1 = list()
        dress_suit2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[5]:
                if each[1] in (hmin, hmax):
                    dress_suit1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    dress_suit2.append(each)
        else:
            for each in b[5]:
                if each[1] in (hmin, hmax):
                    dress_suit1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    dress_suit2.append(each)
        main1.append(dress_suit1)
        main2.append(dress_suit2)

        # 西装套装
        suit1 = list()
        suit2= list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[6]:
                if each[1] in (hmin, hmax):
                    suit1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    suit2.append(each)
        else:
            for each in b[6]:
                if each[1] in (hmin, hmax):
                    suit1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    suit2.append(each)
        main1.append(suit1)
        main2.append(suit2)

        # 裤装
        trousers1 = list()
        trousers2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[7]:
                if each[1] in (hmin, hmax):
                    trousers1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    trousers2.append(each)
        else:
            for each in b[7]:
                if each[1] in (hmin, hmax):
                    trousers1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    trousers2.append(each)
        main1.append(trousers1)
        main2.append(trousers2)

        # 裙装
        skirt1 = list()
        skirt2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[8]:
                if each[1] in (hmin, hmax):
                    skirt1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    skirt2.append(each)
        else:
            for each in b[8]:
                if each[1] in (hmin, hmax):
                    skirt1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    skirt2.append(each)
        main1.append(skirt1)
        main2.append(skirt2)

        # 鞋子
        shoes1 = list()
        shoes2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[9]:
                if each[1] in (hmin, hmax):
                    shoes1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    shoes2.append(each)
        else:
            for each in b[9]:
                if each[1] in (hmin, hmax):
                    shoes1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    shoes2.append(each)
        main1.append(shoes1)
        main2.append(shoes2)

        # 配饰
        accessories1 = list()
        accessories2 = list()
        if a[0] <= 140 or a[0] >= 280:
            for each in b[10]:
                if each[1] in (hmin, hmax):
                    accessories1.append(each)
                if each[1] >= 140 and each[1] <= 280:
                    accessories2.append(each)
        else:
            for each in b[10]:
                if each[1] in (hmin, hmax):
                    accessories1.append(each)
                if float(each[1]) < 140 or float(each[1]) > 280:
                    accessories2.append(each)
        main1.append(accessories1)
        main2.append(accessories2)

    # 2主题色 临近二色
    else:
        main3 = b

    scheme.append(main0)
    scheme.append(main1)
    scheme.append(main2)
    scheme.append(main3)
    return scheme

'''
coat = list()

for h in range(0,18):
    for s in range(0,10):
        for l in range(0,10):
            a = 20*h
            b = 0.1*s
            c = 0.1*l
            coat.append(['1111111',a,b,c])

tops = []

a = [240.00, 0.55, 0.55]

b = [coat]

array = color_match(a, b)

for i in array:
    print(len(i))

for i in array:
    for j in i:
        print(len(j))

for i in array:
    for j in i:
        print(j)
'''







