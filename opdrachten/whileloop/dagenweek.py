dagen = ["maandag", "dinsdag", "woensdag", "donderdag","vrijdag","zaterdag","zondag"]
dag = 0
counter = 0

gekozendag = input ("Kies een dag!(geen hoofdletters gebruiken)\n")
if gekozendag == "maandag":
    dag = 1
elif gekozendag == "dinsdag":
    dag = 2
elif gekozendag == "woensdag":
    dag = 3
elif gekozendag == "donderdag":
    dag = 4
elif gekozendag == "vrijdag":
    dag = 5
elif gekozendag == "zaterdag":
    dag = 6
elif gekozendag == "zondag":
    dag = 7
else:
    print("dat is geen dag van de week!")


while dag > counter:
    print (dagen[(counter)])
    counter += 1

