tries = 1
antwoord = ""
while not antwoord == "quit":
    antwoord = input(f"[{tries}] Wat is het codewoord?\n")
    tries += 1


print (f"Je hebt {tries} keer geprobeerd!")
print("En eindelijk gewonnen!")