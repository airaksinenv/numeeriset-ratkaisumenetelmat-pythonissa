# Yhtälön numeeriset ratkaisumenetelmät pythonissa

-Valtteri Airaksinen


## Johdanto

Tämän projektin tarkoituksena on toteuttaa erilaisia numeerisia ratkaisumenetelmiä pythonissa ja testailla niitä.

Implementoidut ja testatut menetelmät:

- Jakovälimenetelmä
- Falsi-menetelmä
- Newton-Raphson-menetelmä
- Sekanttimenetelmä

Implementoidut funktiot löytyvät tiedostosta `funcs.py` ja niiden testaamiset tiedostosta `testing.ipynb`


---

### Jakovälimenetelmä

Jakovälimenetelmä on numeerinen menetelmä, jota käytetään yhtälön juuren (eli funktion nollakohdan) etsimiseen. Menetelmä perustuu siihen, että jos funktion f(x) arvot ovat eri merkkiset kahdessa kohdassa, niiden välissä on vähintään yksi juuri.

Jakovälimenetelmä on hidas, mutta hyvin luotettava, koska se ei vaadi derivaattaa eikä voi mennä harhaan, jos lähtöväli on valittu oikein. Menetelmä etenee hitaasti, koska se puolittaa välin jokaisella askeleella riippumatta funktion muodosta.

Tämä menetelmä on niin sanottu "bracketing" menetelmä, koska se löytää nollan, etsimällä välin, jonka päissä funktion arvot ovat vastakkaisia. Menetelmä toimii ainoastaan, jos funktio on jatkuva välin sisällä ja sen arvojen merkit ovat erilaiset välin päissä, sillä vain tällöin voidaan taata, että nolla sijaitsee välin sisällä.

### Falsi-menetelmä

Falsi-menetelmä on optimoitu versio jakovälimenetelmästä, koska se käyttää älykkäämpää tapaa valita seuraava iterointipiste.

Menetelmä käyttää lineaarista interpolointia ja valitsee pisteen lähempänä nollaa olevaa kohtaa. Se etenee nopeammin, koska se valitsee fiksumman väliarvon lineaarisen approksimaation perusteella.

Falsi-menetelmä ei kuitenkaan ole täydellinen, sillä se voi joissakin tapauksissa hidastua, jos funktio on vahvasti epäsymmetrinen

Kiteytettynä falsi-menetelmä parantaa jakovälimenetelmää siinä mielessä, että se käyttää ei vain välin päätepisteitä, vaan myös arvioi väliä tarkemmin interpoloinnin avulla.

### Newton-Raphson-menetelmä

Newton-Raphson-menetelmä on tehokas numeerinen menetelmä, joka perustuu funktion tangentin käyttäytymiseen juurensa ympäristössä. Menetelmä etsii funktion juurta lähestymällä sitä iteratiivisesti, jossa uusi arvio juuresta saadaan edellisestä arvioista, funktion arvosta ja sen derivaatasta.

Menetelmä konvergoituu yleensä nopeasti, erityisesti kun alkuarvaus on lähellä oikeaa juurta ja funktio on hyvin käyttäytyvä. Newton-Raphson-menetelmän etuna on sen nopea konvergenssi, mutta se voi epäonnistua, jos alkuarvaus on huono, derivaatta on nolla jollain arvolla tai funktio sisältää paikallisia minimejä tai maksimejä, jolloin se voi jäädä jumiin väärään ratkaisuun.

### Sekanttimenetelmä

Sekanttimenetelmä on numeerinen menetelmä, joka on samankaltainen kuin Newton-Raphson, mutta se ei vaadi funktion derivaatan laskemista. Sen sijaan menetelmä käyttää kahta peräkkäistä pistettä ja arvioi derivaatan sen perusteella. Tämä tekee menetelmästä kätevän, kun derivaatan laskeminen on hankalaa tai ei ole saatavilla.

Sekanttimenetelmä voi olla hyödyllinen, kun derivaatan laskeminen on hankalaa. Se voi kuitenkin olla hitaampi ja epävarmempi kuin Newton-Raphson, erityisesti huonosti käyttäytyvillä funktioilla. Menetelmä vaatii kaksi alkuarvausta ja voi olla herkkä niiden valinnalle.