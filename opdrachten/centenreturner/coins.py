# name of student: Jurre
# number of student: 99066617
# purpose of program: centen teruggave
# function of program: centen teruggaven
# structure of program: python

toPay = int(float(input('Hoeveel u moet betalen: '))* 100) #te betalen
payed = int(float(input('Hoeveel er is betaald: ')) * 100) #betaalt
change = payed - toPay #
#berekent hoeveel wisselgeld er in totaal over is in centen.

if change > 0:
  #bekijt of er uberhaupt wisselgeld is.
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #
    #deelt het wisselgeld door de muntwaarden om zo te berekenen hoeveel munten er nog zijn van die waarden.

    if nrCoins > 0: #
      print('maximale truggaven: ', nrCoins, ' munten van ', coinValue, ' cent!' ) #Laat zien hoeveel je noeg moet teruggeven van een bepaale muntwaarde.
      nrCoinsReturned = int(input('Hoeveel munten van ' + str(coinValue) +  ' wilt u terug?\n ')) #vraagt hoeveel de klant terugwil van die munt.
      change -= nrCoinsReturned * coinValue #Hoeveel munten de klant bepaalt heeft om te nemen wordt van het overige wisselgeld afgehaald.



# comment on code below:
    if coinValue == 500:
        coinValue = 300
        VijfReturned = nrCoinsReturned
    elif coinValue == 300:
        coinValue = 200
        DrieReturned = nrCoinsReturned
    elif coinValue == 200:
        coinValue = 50
        TweeReturned = nrCoinsReturned
    elif coinValue == 50:
        coinValue = 20
        VijftigReturned = nrCoinsReturned
    elif coinValue == 20:
        coinValue = 10
        TwintigReturned = nrCoinsReturned
    elif coinValue == 10:
        coinValue = 5
        TienReturned = nrCoinsReturned
    elif coinValue == 5:
        coinValue = 2
        VijfCentReturned = nrCoinsReturned
    elif coinValue == 2:
        TweeCentReturned = nrCoinsReturned
        coinValue = 1
    else:
        coinValue = 0

#zorgt ervoor dat je steeds muten van kleinere waardes in kan leveren.


if change > 0: #
  print('U heeft nog: ', str(change) + ' centen, en dus niet genoeg teruggegeven!')
#geeft aan of je nog geld niet hebt teruggewisseld en hoeveel.
else:
  print('Transactie voltooid!')

if VijfReturned > 0:
  print(f"5 Euromunten teruggegeven: [{VijfReturned}]")
if DrieReturned > 0:
  print(f"3 Euromunten teruggegeven: [{DrieReturned}]")
if TweeReturned > 0:
  print(f"2 Euromunten teruggegeven: [{TweeReturned}]")
if VijftigReturned > 0:
  print(f"50 Cent euromunten teruggegeven: [{VijftigReturned}]")
if TwintigReturned > 0:
    print(f"20 Cent euromunten teruggegeven: [{TwintigReturned}]")
if TienReturned > 0:
    print(f"10 Cent euromunten teruggegeven: [{TienReturned}]")
if VijfCentReturned > 0:
    print(f"5 Cent euromunten teruggegeven: [{VijfCentReturned}]")
if TweeCentReturned > 0:
    print(f"2 Cent euromunten teruggegeven: [{TweeCentReturned}]")


##print(EenReturned)