import random

ordlista = ["katt", "hund", "fisk", "häst", "ko", "giraff", "apa", "krokodil", "haj", "pingvin"]
ordet = random.choice(ordlista)
gissade_bokstäver = []
fel_bokstäver = []
gissningar = 10
len_ordet = len(ordet)
shown_word = "*"*len_ordet
print("Välkommen till gissa ordet!")
print(f"Du ska gissa ett ord på {len_ordet} bokstäver")

def guess_word(letter):
    if letter in ordet:
        return True
    else:
        return False

while gissningar != 0:

    print(f"Felgissningar: {fel_bokstäver}")
    if shown_word == ordet:
        print("Du vann!")
        break
    print(shown_word)
    print("\n\n")
    bokstav = input("Gissa på en bokstav: ")
    if guess_word(bokstav):
        print("Rätt!")
        gissade_bokstäver.append(bokstav)
        for i in range(0, len_ordet):
            if bokstav == ordet[i]:
                shown_word = shown_word[:i] + bokstav + shown_word[i+1:]

    else:
        print("Fel!")
        gissningar -= 1
        fel_bokstäver.append(bokstav)
        print(f"Du har {gissningar} felgissningar kvar")

if gissningar == 0:
    print("Du har inga fler gissningar. Spelet är slut.")
else:
    print(f"Du hittade ordet som var {ordet}")

