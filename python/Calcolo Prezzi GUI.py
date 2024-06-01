'''
@autor: Francesco Ciociola - https://kekko01.altervista.org
@version: 1.1
2024 GitHub: https://GitHub.com/Kekko01
'''

import tkinter as tk
from random import randint
from Calcolo_Prezzi import calcolo

def entry_numsconti():
    if int(numsconti.get()) > entry_sconti.__len__() and int(numsconti.get()) >= 0:
        etichetta_sconto = tk.Label(root, text=f"Sconto {entry_sconti.__len__() + 1} (es: {randint(1, 99)}%):")
        etichetta_sconto.grid(row=3, column=entry_sconti.__len__() * 2)
        sconto = tk.Entry(root, width=5)
        sconto.grid(row=3, column=entry_sconti.__len__() * 2 + 1)
        entry_etichette_sconti.append(etichetta_sconto)
        entry_sconti.append(sconto)
    elif int(numsconti.get()) < entry_sconti.__len__() and int(numsconti.get()) >= 0:
        etichetta_eliminata = entry_etichette_sconti.pop()
        etichetta_eliminata.destroy()
        sconto_eliminato = entry_sconti.pop()
        sconto_eliminato.destroy()

def calcola_risultato():
    error_perc_guadagno.destroy()
    error_perc_sconti.destroy()
    error_importo.destroy()
    totale.destroy()

    errors = False

    try:
        perc_guadagno = float(percguadagno.get().replace("%", "")) / 100
    except Exception:
        error_perc_guadagno.grid(row=8, column=0, columnspan=2)
        errors = True


    try:
        sconti = [
            float(sconto.get().replace("%", "")) / 100
            for sconto in entry_sconti
        ]
    except Exception:
        error_perc_sconti.grid(row=9, column=0, columnspan=2)
        errors = True
    

    try:
        importo_val = float(importo.get())
    except Exception:
        error_importo.grid(row=10, column=0, columnspan=2)
        errors = True
    
    if errors:
        return
    
    iva_val = iva.get(iva.curselection()).replace("%", "")
    iva_val = float(iva_val) / 100
    totale = tk.Label(root, text=str(calcolo(perc_guadagno, sconti, iva_val, importo_val)))
    totale.grid(row=7, column=1, columnspan=2)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calcolo Prezzi")
    root.geometry("800x600")
    #root.resizable(False, False)

    titolo = tk.Label(root, text="Calcolo Prezzi", font=("Arial", 50))
    titolo.grid(row=0, column=2, columnspan=2)
    
    etichetta_percguadagno = tk.Label(root, text="Percentuale di guadagno (es: 20%):")
    etichetta_percguadagno.grid(row=1, column=0)
    percguadagno = tk.Entry(root)
    percguadagno.grid(row=1, column=1, columnspan=2)
    
    etichetta_numsconti = tk.Label(root, text="Numero di sconti da fare:")
    etichetta_numsconti.grid(row=2, column=0)
    entry_etichette_sconti = []
    entry_sconti = []
    numsconti = tk.Spinbox(root, from_=0, to=10, command=entry_numsconti)
    numsconti.grid(row=2, column=1, columnspan=2)

    etichetta_iva = tk.Label(root, text="IVA da applicare:")
    etichetta_iva.grid(row=4, column=0)
    iva = tk.Listbox(root, selectmode=tk.SINGLE, height=4)
    iva.insert(0, "22%")
    iva.insert(1, "10%")
    iva.insert(2, "5%")
    iva.insert(3, "4%")
    iva.select_set(0)
    iva.grid(row=4, column=1, columnspan=2)

    etichetta_importo = tk.Label(root, text="Importo del prezzo del fornitore: (es: 100.00)")
    etichetta_importo.grid(row=5, column=0)
    importo = tk.Entry(root)
    importo.grid(row=5, column=1, columnspan=2)

    bottone_calcola = tk.Button(root, text="Calcola", command=calcola_risultato)
    bottone_calcola.grid(row=6, column=1, columnspan=2)
    
    etichetta_totale = tk.Label(root, text="Totale:")
    etichetta_totale.grid(row=7, column=0)
    

    error_perc_guadagno = tk.Label(root, text="Errore: la percentuale di guadagno non e' valida", fg="red")

    error_perc_sconti = tk.Label(root, text="Errore: la o le percentuali di uno degli sconti non sono validi", fg="red")

    error_importo = tk.Label(root, text="Errore: l'importo non e' valido", fg="red")

    root.mainloop()