from collections import Counter
from typing import List, Tuple
from ..model.estrazione import Estrazione

def calcola_frequenze(estrazioni: List[Estrazione]) -> List[int]:
    counter = Counter(n for e in estrazioni for n in e.numeri)
    return [num for num, _ in counter.most_common()]

def analisi_ritardi(estrazioni: List[Estrazione]) -> List[Tuple[int, int]]:
    ultima_data = max(e.data for e in estrazioni)
    ritardi = {}
    for num in range(1, 91):
        estratti = [e for e in estrazioni if num in e.numeri]
        ritardi[num] = (ultima_data - max(e.data for e in estratti)).days if estratti else 0
    return sorted(ritardi.items(), key=lambda x: x[1], reverse=True)

def analisi_somme(estrazioni: List[Estrazione]) -> List[int]:
    somme = [sum(e.numeri) for e in estrazioni]
    media = sum(somme) / len(somme)
    return [n for e in estrazioni for n in e.numeri if abs(sum(e.numeri) - media) < 15]

def analisi_parita(estrazioni: List[Estrazione]) -> List[int]:
    pari = sum(1 for e in estrazioni for n in e.numeri if n % 2 == 0)
    return [n for n in range(1, 91) if n % 2 == (0 if pari > len(estrazioni)*3 else 1)]

def analisi_decine(estrazioni: List[Estrazione]) -> List[int]:
    decine = Counter((n-1)//10 for e in estrazioni for n in e.numeri)
    return [n for n in range(1, 91) if (n-1)//10 in [d for d, _ in decine.most_common()[:2]]]

def analisi_sequenze(estrazioni: List[Estrazione]) -> List[int]:
    return [n for e in estrazioni for n in e.numeri if any(abs(n - m) == 1 for m in e.numeri)]
