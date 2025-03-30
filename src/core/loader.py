from pathlib import Path
import csv
from datetime import datetime
from collections import namedtuple

Estrazione = namedtuple('Estrazione', ['data', 'numeri', 'jolly', 'supers'])

def load_estrazioni_multifile(data_folder):
    estrazioni = []
    for csv_file in Path(data_folder).glob("*.csv"):
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                data = datetime.strptime(row[0], "%d/%m/%Y")
                numeri = list(map(int, row[1:7]))
                jolly = int(row[7])
                supers = int(row[8])
                estrazioni.append(Estrazione(data, numeri, jolly, supers))
    return sorted(estrazioni, key=lambda x: x.data)

def load_estrazioni_filtered(data_folder, start_year=None):
    estrazioni = load_estrazioni_multifile(data_folder)
    if start_year:
        return [e for e in estrazioni if e.data.year >= start_year]
    return estrazioni
