# Yhtälön numeeriset ratkaisumenetelmät pythonissa

-Valtteri Airaksinen

---

## Johdanto

Tämän projektin tarkoituksena on toteuttaa erilaisia numeerisia ratkaisumenetelmiä pythonissa ja testailla niitä

Implementoidut ja testatut menetelmät:

- Jakovälimenetelmä

---

### Jakovälimenetelmä

Jakovälimenetelmä on numeerinen menetelmä, jota käytetään yhtälön juuren (eli funktion nollakohdan) etsimiseen. Menetelmä perustuu siihen, että jos funktion f(x) arvot ovat eri merkkiset kahdessa kohdassa, niiden välissä on vähintään yksi juuri.

Jakovälimenetelmä on hidas, mutta hyvin luotettava, koska se ei vaadi derivaattaa eikä voi mennä harhaan, jos lähtöväli on valittu oikein.