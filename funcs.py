# Menetelmien implementointi pythoniin

# Jakovälimenetelmä
def bisection_method(func, a, b, error_accept):
    """
    Jakovälimenetelmä (bisection method) funktion juuren etsimiseen.

    Parametrit:
    func (function): Funktio, jonka juuri halutaan löytää (esim. lambda x: x**2 - 2).
    a (float): Välin vasen raja.
    b (float): Välin oikea raja.
    error_accept (float): Hyväksyttävän virheen raja.

    Palauttaa:
    float: Arvioitu juuren arvo, jos se löytyy annetulla tarkkuudella.
    
    Heittää:
    ValueError: Jos funktion arvo ei vaihda merkkiä annetulla välillä.
    """
    
    # Tarkistetaan, että funktio vaihtaa merkkiä annetulla välillä
    if func(a) * func(b) >= 0:
        raise ValueError("Ei juurta tai useita juuria annetulla välillä, jakomenetelmä ei toimi.")

    # Alustetaan virheväli (b - a)
    error = abs(b - a)

    # Iteroidaan, kunnes virhe on hyväksyttävän rajan sisällä
    while error > error_accept:
        # Lasketaan välin puoliväli
        c = (b + a) / 2

        # Tarkistetaan, kummalla puolella juuri sijaitsee
        if func(c) * func(a) < 0:
            # Juuri on vasemmalla puolella, päivitetään b
            b = c
        else:
            # Juuri on oikealla puolella, päivitetään a
            a = c

        # Päivitetään virhe uuden välin perusteella
        error = abs(b - a)

        # Tulostetaan tilannetietoa suomeksi
        print(f"Nykyinen virhe: {error}")
        print(f"Uusi alaraja a: {a}, uusi yläraja b: {b}")

    # Palautetaan arvioitu juuri (välin keskipiste)
    return (a + b) / 2

# Falsi-menetelmä
def regula_falsi(func, a, b, error_accept):
    """
    Falsi-menetelmä (Regula Falsi) funktion juuren etsimiseen.

    Parametrit:
    func (function): Funktio, jonka juuri halutaan löytää (esim. lambda x: x**2 - 2).
    a (float): Välin vasen raja.
    b (float): Välin oikea raja.
    error_accept (float): Hyväksyttävän virheen raja.

    Palauttaa:
    float: Arvioitu juuren arvo, jos se löytyy annetulla tarkkuudella.
    
    Heittää:
    ValueError: Jos funktion arvo ei vaihda merkkiä annetulla välillä.
    """
    
    # Tarkistetaan, että funktio vaihtaa merkkiä annetulla välillä
    if func(a) * func(b) >= 0:
        raise ValueError("Ei juurta tai useita juuria annetulla välillä, menetelmä ei toimi.")

    error = abs(b - a)  # Alustetaan virhevälillä (b - a)
    c = a  # Alustetaan c muuttuja
    
    while error > error_accept:
        # Lasketaan uusi piste c käyttäen regula falsi -kaavaa
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        
        # Tulostetaan iteroinnin eteneminen
        print(f"Nykyinen arvio juurelle: {c}")
        print(f"Nykyinen virhe: {error}")
        print(f"Uusi alaraja a: {a}, uusi yläraja b: {b}\n")
        
        # Tarkistetaan, onko juuri löytynyt tarkasti
        if func(c) == 0:
            break
        
        # Päivitetään väli samalla tavalla kuin jakovälimenetelmässä
        elif func(c) * func(a) < 0:
            b = c  # Juuri on vasemmalla puolella
        else:
            a = c  # Juuri on oikealla puolella
        
        # Päivitetään virhe uuden välin perusteella
        error = abs(b - a)

    return c  # Palautetaan arvioitu juuri

# Newton raphson -menetelmä
def newton_raphson(func, func_prime, x0, error_accept, max_iter=100):
    """
    Newton-Raphson-menetelmä funktion juuren etsimiseen.

    Parametrit:
    func (function): Funktio, jonka juuri halutaan löytää (esim. lambda x: x**2 - 2).
    func_prime (function): Funktion derivoitu versio (derivaatta).
    x0 (float): Alkuarvaus juurelle.
    error_accept (float): Hyväksyttävän virheen raja.
    max_iter (int): Maksimimäärä iteraatioita (vapaaehtoinen, oletus 100).

    Palauttaa:
    float: Arvioitu juuren arvo, jos se löytyy annetulla tarkkuudella.
    
    Heittää:
    ValueError: Jos konvergenssia ei saavuteta annetussa maksimimäärässä iteraatioita.
    """
    
    x = x0  # Alustetaan alkupiste
    for i in range(max_iter):
        fx = func(x)  # Funktioarvo
        fx_prime = func_prime(x)  # Derivaatta-arvo
        
        # Tarkistetaan, ettei derivaatta ole nolla (jotta voidaan jakaa sillä)
        if fx_prime == 0:
            raise ValueError(f"Derivaatta on nolla kohdassa x = {x}, menetelmä ei toimi.")
        
        # Lasketaan seuraava arvio juurelle
        x_new = x - fx / fx_prime
        
        # Lasketaan virhe
        error = abs(x_new - x)
        
        # Tulostetaan iteroinnin eteneminen
        print(f"Iteraatio {i+1}: Arvio juurelle: {x_new}")
        print(f"Nykyinen virhe: {error}\n")
        
        # Tarkistetaan, onko virhe tarpeeksi pieni
        if error < error_accept:
            return x_new  # Palautetaan arvioitu juuri
        
        # Päivitetään arvio seuraavalle iteraatiolle
        x = x_new
    
    # Jos konvergenssia ei saavuteta, heitetään virhe
    raise ValueError(f"Konvergenssia ei saavutettu {max_iter} iteraation aikana.")

# Sekantti -menetelmä
def secant(func, x0, x1, error_accept, max_iter=100):
    """
    Secant-menetelmä funktion juuren etsimiseen ilman derivaatan laskemista.

    Parametrit:
    func (function): Funktio, jonka juuri halutaan löytää (esim. lambda x: x**2 - 2).
    x0 (float): Ensimmäinen arvio juuresta.
    x1 (float): Toinen arvio juuresta.
    error_accept (float): Hyväksyttävän virheen raja.
    max_iter (int): Maksimimäärä iteraatioita ennen virheen heittämistä.

    Palauttaa:
    float: Arvioitu juuren arvo, jos se löytyy annetulla tarkkuudella.
    
    Heittää:
    ValueError: Jos menetelmä ei konvergoidu annetun virherajan puitteissa.
    """
    
    error = abs(x1 - x0)  # Alustetaan virhe
    iter_count = 0  # Iteraatiolaskuri

    while error > error_accept and iter_count < max_iter:
        # Lasketaan uusi arvio käyttäen secant-kaavaa
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        
        # Päivitetään virhe
        error = abs(x2 - x1)

        # Päivitetään arvot
        x0, x1 = x1, x2
        iter_count += 1

        # Tulostetaan iteroinnin eteneminen
        print(f"Nykyinen arvio juurelle: {x2}")
        print(f"Nykyinen virhe: {error}")
        print(f"Uusi arvio: {x2}\n")
    
    # Tarkistetaan, onko menetelmä konvergoitunut
    if iter_count >= max_iter:
        raise ValueError("Menetelmä ei konvergoitunut annetun iteraatiomäärän puitteissa.")

    return x2  # Palautetaan arvioitu juuri