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

def vis_alle():
    for person in telefonbok:
        print (f"Navn: {person["navn"]}, Nummer: {person["nummer"]}")
vis_alle()