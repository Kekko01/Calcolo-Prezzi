'''
@autor: Francesco Ciociola - https://kekko01.altervista.org
@version: 1.1
2019 GitHub: https://GitHub.com/Kekko01
'''
def main():
    percguadagno=float(input("Ciao! Prima di tutto inserisci la percentuale di guadagno (senza il %): "))
    percguadagno/=100

    numerosconti=int(input("Inserisci il numero (intero) di sconti da fare: "))
    sconti=[]
    if numerosconti>0:
        for i in range(numerosconti):
            sconto=float(input("Inserisci lo sconto numero {} (senza il %): ".format(i+1)))
            sconto/=100
            sconti.append(sconto)

    iva=int(input("Inserire l'IVA da applicare (metti numero intero, es: 22% = 22): "))
    iva=float(iva)/100

    importo=1
    while importo!=0:
        importo=float(input("Inserisci l'importo del prezzo del fornitore (se e' con la virgola, usare il punto): "))

        totale=importo
        if numerosconti>0:
            for i in range(numerosconti):
                totale=totale-totale*sconti[i]
        totale=totale+totale*percguadagno
        totale=totale+totale*iva

        print("Il prezzo di vendita di",importo,"euro con perc. di guadagno al",percguadagno*100,"%, l'IVA al 22% e",numerosconti,"sconto/i e':",totale)
main()
