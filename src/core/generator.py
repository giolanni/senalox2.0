import random
from collections import defaultdict
from .analyzer import calcola_frequenze, analisi_ritardi

def genera_pool_pesato(estrazioni, strategy_weights):
    pool = defaultdict(float)
    
    # Frequenza
    if strategy_weights['frequenza'] > 0:
        frequenze = calcola_frequenze(estrazioni)
        for num, peso in frequenze.items():
            pool[num] += peso * strategy_weights['frequenza']
    
    # Ritardi
    if strategy_weights['ritardo'] > 0:
        ritardi = analisi_ritardi(estrazioni)
        for num, ritardo in ritardi:
            pool[num] += ritardo * strategy_weights['ritardo']
    
    # Altre strategie possono essere aggiunte qui
    
    return sorted(pool.items(), key=lambda x: x[1], reverse=True)

def genera_sestina_pesata(estrazioni, strategy_weights=None):
    weights = strategy_weights or {'frequenza': 0.5, 'ritardo': 0.5}
    pool = genera_pool_pesato(estrazioni, weights)
    return [num for num, _ in pool[:6]]
