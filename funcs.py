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