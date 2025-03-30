#!/usr/bin/env python3
# exec_gui.py - Punto d'ingresso principale

import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

def main():
    try:
        from gui.main_window import MainWindow
        start_year = int(sys.argv[1]) if len(sys.argv) > 1 else None
        root = tk.Tk()
        MainWindow(root, start_year)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Errore Critico", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
