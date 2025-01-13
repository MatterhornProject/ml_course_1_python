def aktualizacja_wynagrodzenia(wynagrodzenia: dict) -> dict:
    """
    Funkcja, która aktualizuje niskie wynagrodzenia

    Args
        wynagrodzenia: slownik id_pracownika: wynagrodzenia
    Return
        Zaktualizowana slownik plac
    Exceptions
    Exception - jeżeli dlugosc slownika wynosi 0.
    TypeError - jezeli wartosc w slowniku nie jest liczba.
    """
    if len(wynagrodzenia)==0:
        raise Exception("Place nie moga byc puste.")
    for id, kwota in wynagrodzenia.items():
        if type(kwota) not in (float, int):
            raise TypeError(f'Pracownik o id {id} ma niepoprawna kwote wyngrodzenia.')
    suma = sum(wynagrodzenia.values())
    srednia = suma / len(wynagrodzenia)

    for id, kwota in wynagrodzenia.items():
        if kwota <= 0.8 * srednia:
            nowa_kwota = 1.2 * kwota 
            wynagrodzenia[id] = nowa_kwota
            print(f'Zaktualizowano wynagrodzenie pracownika o id {id} z {kwota} na {nowa_kwota}')
        elif kwota <= 0.9 * srednia:
            nowa_kwota = 1.1 * kwota
            wynagrodzenia[id] = nowa_kwota
            print(f'Zaktualizowano wyngardzoenie pracownika o id {id} z {kwota} na {nowa_kwota}')
        ## Usprawnienie:
        # if nowa_kwota > kwota:
            # wynagrodzenia[id] = nowa_kwota
            # print(f'Zaktualizowano wyngardzoenie pracownika o id {id} z {kwota} na {nowa_kwota}')
    suma_nowa = sum(wynagrodzenia.values())
    srednia_nowa = suma_nowa / len(wynagrodzenia)
    print(f'Zaktualizowano place. Poprzednia srednia zespolu wynosila {srednia}.\n Nowa srednia wynosi {srednia_nowa}.')
    return wynagrodzenia   

wyn = {1: 1500,
       2: 4500,
       6: 20000,
       7: 10000,
       10: 7800}
print(aktualizacja_wynagrodzenia(wyn))