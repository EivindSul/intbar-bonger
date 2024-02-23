# Intbar-bonger
## Beskrivelse
Program til å lage PDF'er med bonger til utskrift. 
Lager forside, bakside, og et sjekke-ark med de samme bongene.

## Bruk
TODO:
Gjør den brukbar

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
