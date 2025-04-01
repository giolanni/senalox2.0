import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from src.core.loader import load_estrazioni_multifile, filtra_per_data
from src.core.generator import GeneratorePesato

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Senalox 2.0")
        self.geometry("800x600")
        
        self.estrazioni_full = []
        self.estrazioni_2009 = []
        self.generatore = None
        
        self.crea_interfaccia()
        self.carica_dati()

    def crea_interfaccia(self):
        # Frame principale
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Pulsanti modalità
        ttk.Button(main_frame, text="Modalità FULL", 
                 command=lambda: self.avvia_generazione('full')).pack(pady=5)
        ttk.Button(main_frame, text="Modalità 2009", 
                 command=lambda: self.avvia_generazione('2009')).pack(pady=5)
        
        # Risultato
        self.risultato_label = ttk.Label(main_frame, text="", font=('Arial', 14))
        self.risultato_label.pack(pady=20)
        
        # Console log
        self.log_text = tk.Text(main_frame, height=10, state='disabled')
        self.log_text.pack(fill='x')

    def carica_dati(self):
        self.log("Caricamento dati in corso...")
        try:
            self.estrazioni_full = load_estrazioni_multifile()
            data_2009 = date(2009, 7, 1)
            self.estrazioni_2009 = filtra_per_data(self.estrazioni_full, data_2009)
            self.log("Dati caricati correttamente!")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def avvia_generazione(self, modalita):
        estrazioni = self.estrazioni_2009 if modalita == '2009' else self.estrazioni_full
        if not estrazioni:
            messagebox.showwarning("Attenzione", "Nessun dato disponibile")
            return
            
        try:
            self.generatore = GeneratorePesato(estrazioni)
            sestina = self.generatore.genera_sestina_pesata()
            self.risultato_label.config(
                text=f"Sestina generata ({modalita}):\n{', '.join(map(str, sestina))}"
            )
            self.log(f"Generazione {modalita} completata")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def log(self, messaggio):
        self.log_text.configure(state='normal')
        self.log_text.insert('end', f"> {messaggio}\n")
        self.log_text.see('end')
        self.log_text.configure(state='disabled')

