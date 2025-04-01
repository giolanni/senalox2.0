from collections import defaultdict
from typing import List
import random

from src.model.estrazione import Estrazione

class GeneratorePesato:
    def __init__(self, estrazioni: List[Estrazione]):
        self.estrazioni = estrazioni
        self.pesi_strategie = {
            'frequenza': 0.4,
            'ritardo': 0.3,
            'somma': 0.2,
            'parita': 0.1
        }
        self._precalcola_statistiche()

    def _precalcola_statistiche(self):
        """Calcola tutte le statistiche necessarie"""
        self.frequenze = defaultdict(int)
        self.ritardi = defaultdict(int)
        ultima_data = max(e.data for e in self.estrazioni)
        
        for e in self.estrazioni:
            for n in e.numeri:
                self.frequenze[n] += 1
                if n not in self.ritardi or e.data > self.ritardi[n]:
                    self.ritardi[n] = e.data
                    
        for n in self.ritardi:
            self.ritardi[n] = (ultima_data - self.ritardi[n]).days

    def genera_sestina_pesata(self) -> List[int]:
        """Genera una sestina combinando le strategie con pesi"""
        pool = []
        
        # Strategia: Frequenza
        freq_nums = sorted(self.frequenze.items(), key=lambda x: -x[1])[:20]
        pool += [n for n, _ in freq_nums] * int(self.pesi_strategie['frequenza'] * 100)
        
        # Strategia: Ritardo
        ritardo_nums = sorted(self.ritardi.items(), key=lambda x: -x[1])[:15]
        pool += [n for n, _ in ritardo_nums] * int(self.pesi_strategie['ritardo'] * 100)
        
        # Strategia: Somma
        somme = [sum(e.numeri) for e in self.estrazioni]
        media_somme = sum(somme) / len(somme)
        somma_nums = [n for e in self.estrazioni for n in e.numeri 
                     if abs(sum(e.numeri) - media_somme) < 15]
        pool += somma_nums * int(self.pesi_strategie['somma'] * 100)
        
        # Strategia: Parità
        pari = sum(1 for e in self.estrazioni for n in e.numeri if n % 2 == 0)
        parita_nums = [n for n in range(1, 91) if n % 2 == (0 if pari > len(self.estrazioni)*3 else 1)]
        pool += parita_nums * int(self.pesi_strategie['parita'] * 100)
        
        # Selezione finale
        return sorted(random.sample(pool, 6))
