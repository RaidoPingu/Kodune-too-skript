"""

"""

import random
from datetime import datetime

time = datetime.now() # Kutsume välja 
vormindatud =time.strftime('%d.%m.%Y %H:%M:%S') # Vormindmae aja ära, et oleks nagu vaja 
filename = 'andmed.txt' # Genereeritava faili nimi
arvud =[] # Tühi list kuhu hiljem korjame arvud.
# Siit hakkab faili genereerimise ning kuupäeva ja juhuslike arvude salvestamise kood.

with open(filename, 'w', encoding='utf-8') as f: # Avame faili kirjutamiseks
    f.write(f'Kuupäev: {vormindatud} \n') # Kirjutame kohe kuupäeva faili
    f.write('Arvud: ') # Alustame uuelt realt sõnadega arvud
    count = 0 # Teeme While loopi jaoks counteri
    while count < 20: # While loop juhuslike arvude genereerimiseks
        nr = random.randint(1, 101) # Genereerime juhusliku arvu
        f.write(f' {nr}') # Kirjutame selle arvu faili
        count += 1 # Lisame +1 counterisse.

# Siit alates loeme loodud failist arvud sisse, töötleb ja kuvab neid

    # Loeme faili sisse ja puhastame välja ainult arvud listi

with open(filename, 'r', encoding='utf-8' ) as f:
    contents = f.readlines()[1:] # Loeme faili sisu muutujasse, alates teisest reast
    for parts in contents: # Loop elementide lahti võtmiseks
        parts = parts.split() # Kaotame ära tühikud
        for part in parts: # teine loop mis võtab 1 elemendi
            if part.isdigit(): # Kontrollime kas on tegu arvuga
                arvud.append(int(part)) # Kui on arv lisame loodud tühja listi. 

    #Võtame selle listi ja teem maagiat.

