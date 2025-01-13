def kampania_rezultat():
    czas_kampanii = int(input("Podaj na ile dnie jest zaplanowana kampania:"))
    czas_jaki_minal = int(input("Podaj ile dni kampanii juz sie zakonczyło: "))
    wplywy_total = int(input("Podaj jakie sa szacowane wplywy: "))
    wplywy_aktualne = int(input("Podaj jakie wplywy zaobserwowano do tej pory: "))
    if czas_kampanii<=0:
        return print("Kampania musi trwac co najmniej 1 dzien")
    if czas_jaki_minal <=0:
        return print("Musi minac przynajmniej 1 dzien kampanii")
    srednie_wplywy_total = wplywy_total / czas_kampanii
    srednie_wplywy_aktualne = wplywy_aktualne / czas_jaki_minal
    if srednie_wplywy_aktualne < srednie_wplywy_total:
        return print(f'Aktualne wplywy sa zbyt niskie. Wynosza sredniodziennie {srednie_wplywy_aktualne}, a powinny {srednie_wplywy_total}')
    elif srednie_wplywy_aktualne >= srednie_wplywy_total:
        return print('Wszystko zgodnie z planem')


kampania_rezultat()
input('Press enter to quit')