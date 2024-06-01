'''
@autor: Francesco Ciociola - https://kekko01.altervista.org
@version: 1.1
2024 GitHub: https://GitHub.com/Kekko01
'''

def calcolo(guadagno, sconti, iva, importo):
    if sconti.__len__() > 0:
            for sconto in sconti:
                importo = importo - importo * sconto
    importo = importo + importo * guadagno
    importo = importo + importo * iva
    return importo

def main():
    percguadagno = float(input("Ciao! Prima di tutto inserisci la percentuale di guadagno (senza il %): "))
    percguadagno /= 100

    numerosconti = int(input("Inserisci il numero (intero) di sconti da fare: "))
    sconti = []
    if numerosconti > 0:
        for i in range(numerosconti):
            sconto = float(input(f"Inserisci lo sconto numero {i + 1} (senza il %): "))
            sconto /= 100
            sconti.append(sconto)

    iva = int(input("Inserire l'IVA da applicare (metti numero intero, es: 22% = 22): "))
    iva = float(iva)/100

    importo = 1
    while importo != 0:
        importo = float(input("Inserisci l'importo del prezzo del fornitore (se e' con la virgola, usare il punto): "))

        print("Il prezzo di vendita di", importo, "euro con perc. di guadagno al", percguadagno * 100, "%, l'IVA al", int(iva * 100),"% e", numerosconti, "sconto/i e':", calcolo(percguadagno, sconti, iva, importo))

if __name__ == "__main__":
    main()
