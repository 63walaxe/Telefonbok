# Oppgave 1
telefonbok = []
person1 = {
    "navn": "sverrre",
    "nummer": "46576760"
}
person2 = {
    "navn": "andreas",
    "nummer": "93692597"
}
telefonbok.append(person1)
telefonbok.append(person2)
# Oppgave 2
def vis_alle():
    for person in telefonbok:
        print (f"Navn: {person["navn"]}, Nummer: {person["nummer"]}")
vis_alle()
# Oppgave 3
def legg_til():
    leggtilnavn = input("Skriv inn navn: ")
    leggtilnummer = input("Skriv inn nummer: ")
          
    nyperson = {
    "navn": leggtilnavn,
    "nummer": leggtilnummer
}
    print(f"Navn ble lagt til {nyperson["navn"]}, Nummer ble lagt til {nyperson["nummer"]}")

    telefonbok.append(nyperson)

legg_til()
# Oppgave 4
def søk():
    navnsøk = input("Skriv inn et navn: ")
    for sjekk in telefonbok:
        if navnsøk.lower() == sjekk["navn"].lower():
            print(f"Vi har {sjekk['navn']} i databasen vår, telefonnummer: {sjekk["nummer"]}")
            break
    else:
        print(f"Vi har ikke {navnsøk} i databasen vår")

søk()
# Oppgave 5
while True:
        print("\n1. Vis alle") #/n er det som for det til å se pent ut, lærte det av sverre/jakob/hannah/matthias
        print("2. Legg til ny")
        print("3. Søk")
        print("4. Avslutt")
        valg = input("Hva ønsker du å gjøre? (skriv tall eller navn på valg): ").lower()

        if valg in ("1", "vis alle"):
            vis_alle()
        elif valg in ("2", "legg til ny"):
            legg_til()
        elif valg in ("3", "søk"):
            søk()
        elif valg == "4":
            print("Programmet avsluttes.")
            break
        else:
            print("Ugyldig valg.")
# Oppgave 6