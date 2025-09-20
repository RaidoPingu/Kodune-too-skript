import random
from datetime import datetime

time = datetime.now()
filename = 'andmed.txt'

with open(filename, 'w', encoding='utf-8') as f:
    f.write(f'Kuupäev: {str(time)}')