import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from ..core import loader, analyzer, generator
from ..optimization.strategies import StrategyOptimizer
from .tabs.optimization_tab import OptimizationTab

class MainWindow:
    def __init__(self, master, start_year=None):
        self.master = master
        self.start_year = start_year
        self.estrazioni = loader.load_estrazioni_filtered("./data", start_year)
        self.optimizer = StrategyOptimizer("./data", start_year)
        
        self._configure_window()
        self._create_widgets()

    def _configure_window(self):
        self.master.title("Senalox 2.0 - SuperEnalotto Analyzer")
        self.master.geometry("1200x800")
        self.master.minsize(800, 600)

    def _create_widgets(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both')
        
        self._create_generation_tabs()
        self._create_optimization_tab()
        self._create_analysis_tabs()

    def _create_generation_tabs(self):
        methods = [
            ("Frequenze", lambda: generator.genera_sestina_pesata(self.estrazioni)),
            ("Ritardi", lambda: generator.genera_sestina_pesata(
                self.estrazioni, 
                {'ritardo': 1.0}
            )),
            ("Combinata", lambda: generator.genera_sestina_pesata(
                self.estrazioni, 
                {'frequenza': 0.5, 'ritardo': 0.5}
            ))
        ]
        
        for name, func in methods:
            frame = ttk.Frame(self.notebook)
            self._add_generation_ui(frame, name, func)
            self.notebook.add(frame, text=name)

    def _add_generation_ui(self, frame, title, generator_func):
        ttk.Label(frame, text=title, font=('Arial', 14)).pack(pady=10)
        result_text = tk.Text(frame, height=2, font=('Arial', 12))
        result_text.pack(pady=10)
        
        def generate():
            try:
                numbers = sorted(generator_func())
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, ", ".join(map(str, numbers)))
            except Exception as e:
                messagebox.showerror("Errore", str(e))
                
        ttk.Button(frame, text="Genera", command=generate).pack()

    def _create_optimization_tab(self):
        optimization_frame = OptimizationTab(self.notebook, self.optimizer)
        self.notebook.add(optimization_frame, text="Ottimizzazione")

    def _create_analysis_tabs(self):
        # Implementa le schede di analisi esistenti
        pass
