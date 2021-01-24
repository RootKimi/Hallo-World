
clear

print ("Schachfeld Nummer 1:")
print ("1 Reiskorn")
print ("Die Summe an Reiskörnern ist: 1")

feldnummer = 2
reiskorn = 1
summe = reiskorn

while feldnummer < 65: 
   
    reiskorn = reiskorn * 2
    summe = reiskorn + summe
    print (f"Schachfeld Nummer {feldnummer}:")
    print ("Reiskörner auf dem Feld:")
    print("{:,}".format(reiskorn))

    print (f"Die Summe an Reiskörnern ist:")
    print("{:,}".format(summe))
    feldnummer += 1

#https://www.python-kurs.eu/python3_formatierte_ausgabe.php