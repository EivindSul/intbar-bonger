# Intbar-bonger
## Beskrivelse
Program til å lage PDF'er med bonger til utskrift. 
Lager forside, bakside, og et sjekke-ark med de samme bongene.

## Bruk
For nå brukes programmet kun i terminal.

Installer conda. Jeg anbefaler [miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

Klon prosjektet med git.
```bash
git clone git@github.com:EivindSul/intbar-bonger.git
```
Aktiver conda environment for å installere de nødvendige pakkene.
```bash
# Gå til mappen
cd intbar-bonger

# Aktiver environment
conda env create -f environment.yml
conda activate intbar-bonger-env
```

Nå skal programmet være klart til å kjøres.

Hovedprogrammet heter intbar-bonger.py.

```bash
python intbar-bonger.py
```
Programmet gir en gjennomgang av de forskjellige feltene på bongen.
Om du lar feltet stå tomt, så bruker det standardverdiene som står beskrevet når du kjører programmet.
VÆr obs på at enkelte input kan få bongene til å se stygge ut, for eksempel at "serie" blir mer enn tre tegn langt.

Bongene blir lagret som en pdf-fil i samme mappe.

## Utvikling og vedlikehold
Dette programmet er skrevet i python med hensikten at det skal kunne bli
vedlikeholdt om det en dag slutter å virke.  Alle på MatNat har INF100, og
er derfor noenlunde kjent med python. Allikevel så skriver jeg noen instrukser
for hvordan programmet oppdateres, og hva som sannsynligvis kan fikse det.

Prosjektet inneholder et conda environment, `environment.yml`.
Denne filen forteller conda sammensetnignen av pakker som ble brukt til å
bygge prosjektet, som da skal fortsatt fungere.

For å aktivere `environment.yml`, skriv i terminalen:
```bash
conda env create -f environment.yml
conda activate intbar-bonger-env
```
Dette skal være likt på Linux, Mac og Windows.

Når environment'et er aktivert, så er det bare å prøve å kjøre programmet
og lese feilmeldingene for å finne ut av problemene.  Det kan også være
lurt å oppdatere pakkene og python-versjonen som brukes i programmet.

Etter du er ferdig med arbeid, oppdater `environment.yml` med de nye pakkene,
og avslutt environment'et.
```bash
# Om du har endret pakker:
conda env export --from-history > environment.yml
conda deactivate
```
