import bong_generator

print("For å lage bonger, fyll ut feltene. La dem være tomme for å bruke standardverdiene:")
print("Antall: 50 stk")
print("Serie: A")
print("Beskrivelse: Integrerbar arrangementer")
print("Verdi: 65")
print("Utløpsdato: Om et år.")
print("")

count = input("Hvor mange bonger vil du lage?\n")
series = input("Hvilken serie skal bongene være? Dette er bokstaven som står på bongen\n")
description = input("Hva skal beskrivelsen være? Denne kan for eksempel være hvilket arrangement de skal brukes på.\n")
value = input("Hvor mye er hver bong verdt?\n")
expiration = input("Når skal bongene gå ut? Gi dato i format dd-mm-yyyy\n")

if count == "":
    count = 50
else:
    count = int(count)

if series == "":
    series = "A"

if description == "":
    description = "Integrerbar arrangementer"

if value == "":
    value = 65 
else:
    value = int(value)

if expiration == "":
    expiration = None

bg = bong_generator.BongGenerator(count=count, series=series, value=value, expiration=expiration)
bg.generate_pdf()

