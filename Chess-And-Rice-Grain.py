print ("Schachfeld Nummer 1:")
print ("1 Reiskorn")
print ("Die Summe an Reiskörnern ist: 1")

feldnummer = 2
reiskorn = 1
summe = reiskorn

while feldnummer < 64: 
   
    reiskorn = reiskorn * 2
    summe = reiskorn + summe
    print (f"Schachfeld Nummer {feldnummer}:")
    print (f"{reiskorn} Reiskörner")

    print (f"Die Summe an Reiskörnern ist: {summe}")
    feldnummer += 1