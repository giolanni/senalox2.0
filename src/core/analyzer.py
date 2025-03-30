
from collections import defaultdict

def calcola_frequenze(estrazioni):
    frequenze = defaultdict(int)
    for estrazione in estrazioni:
        for num in estrazione.numeri:
            frequenze[num] += 1
        frequenze[estrazione.jolly] += 1
        frequenze[estrazione.supers] += 1
    return dict(sorted(frequenze.items(), key=lambda x: x[1], reverse=True))

def analisi_ritardi(estrazioni):
    ultima_estrazione = max(e.data for e in estrazioni)
    ritardi = {}
    for e in reversed(estrazioni):
        for num in e.numeri + [e.jolly, e.supers]:
            if num not in ritardi:
                ritardi[num] = (ultima_estrazione - e.data).days
    return sorted(ritardi.items(), key=lambda x: x[1], reverse=True)

# Altre funzioni di analisi...
