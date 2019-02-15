# Šime Martinov - završni pojekt

## Opis projekta
Za svoj završni projekt sam pokušao napraviti aplikaciju "Smart Adventure Park", koja je neka vrsta portala na kojem korisnik može dobiti informacije o aktivnostima u prirodi. Konkretno, postoje dva parka, Paklenica i Zrmanja, u kojima se nude aktivnosti penjanja na stijene i raftinga.

## Kome je aplikacija namjenjena
"Smart Adventure Park" je online aplikacija namjenjena korisnicima koji žele provjeriti kakva se aktivnosti nude u dva parka. Na stranicama koje su im ponuđene mogu pročitati opće informacije o parkovima, pronaći lokacije parkova, pročitati iskustva nekih prijašnjih gostiju, izračunati koliko bi ih koštao jedan takav izlet i pretplatiti se na primanje novosti i ponuda parkova.

## Tehnički aspekti
### Razvojna okolina
U projektu sam koristio standardne prakse koje smo usvojili na predmetu, tako da je projekt strukturiran na način da je glavni dio logike aplikacije u main.py datoteci. Predlošci, css, prijevodi itd koji se pozivaju su odgovarajućim templates, static i translations folderima. Library potrebni za pokretanje aplikacije nalaze se u requirements.txt datoteci.

### Primjenjene tehnike i tehnologije
Od dosadašnjih tehnologija i tehnika s kojima smo se upoznali, koristio sam:
* Prog. jezici: Python, HTML, CSS, JavaScript
* Flask predlošci
* Web forme (za pretplatu na newsletter, doduše, ne šalje zapravo mail nakon potvrde)
* Pozivanje REST servisa (API za vremenske prilike)
* Prijevod
* Bootstrap
* Error handling
* Azure Deployment (o ovome više na dnu)

### API
Aplikacija koristi [openweathermap](https://openweathermap.org/) kao API za dohvat podataka o vremenskim prilikama. S obzirom da API ne nudi podatke za konkretne lokacije parkova, odabrao sam najbliža dostupna mjesta, odnosno Starigrad u slučaju Paklenice i Obrovac u slučaju Zrmanje.
Aplikacija također ima *embeddane* karte s Google-a na kojima su određene lokacije parkova.

### Prijevod
Sve stranice koje se nude korisnicima su dostupne u ENG i HR verzijama.

### Error handling
Aplikacija podržava *handling* dva osnovna tipa greške, 404 i 500, tako da se korisniku prikaže odgovarajuća poruka na ekranu umjesto "ružnog" ispisa kojeg bi inače dobio.

### Azure Deployment
S obzirom da imam Azure account i subscription, pokušao sam *deployati* aplikaciju na Azure. Nažalost, nakon nekoliko pokušaja i dalje nisam uspio doći do faze u kojoj je aplikacija dostupna i stabilna online. Sljedio sam upute s predavanja, ali dobivam *application error* na stranici [https://flask-parks.azurewebsites.net/](https://flask-parks.azurewebsites.net/). Nadam se da ću uspjeti to srediti...
