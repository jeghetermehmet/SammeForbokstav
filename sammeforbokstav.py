personer = {}

inn = "j"
while inn == "j":
    navn = input("Oppgi navn: ")
    alder = input("Oppgi alder: ")
    personer[navn] = alder

    inn = input('Skriv "j" for å taste inn flere navn: ')

bokstav = input("Oppgi en bokstav: ")
while len(bokstav) != 1:
    print("Ugyldig input!")
    bokstav = input("Oppgi en bokstav: ")

bokstav = bokstav.lower()

for key in personer:
    if key[0].lower() == bokstav:
        print(key, personer[key])