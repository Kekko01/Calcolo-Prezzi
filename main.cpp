#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	system("title CALCOLO PREZZI");
	cout<<"Ciao! Prima di tutto inserisci la percentuale di guadagno (senza il %) : ";
	float percguadagno;
	cin>>percguadagno;
	percguadagno/=100;
	
	int numerosconti;
	cout<<"Inserisci il numero (intero) di sconti da fare: ";
	cin>>numerosconti;
	float sconti[numerosconti];
	float sconto;
	if(numerosconti>0){
		for(int i=0; i<numerosconti; i++){
			cout<<"Inserisci lo sconto numero "<<i<<" (senza il %): ";
			cin>>sconto;
			sconto/=100;
			sconti[i]=sconto;
		}
	}
	
	float importo=1;
	while(importo!=0){
		cout<<"\n\nInserisci l'importo del prezzo del fornitore (se e' con la virgola, usare il punto): ";
		cin>>importo;
		
		float totale=importo;
		if(numerosconti>0){
			for(int i=0; i<numerosconti; i++){
				totale=totale-totale*sconti[i];
			}
		}
		totale=totale+totale*percguadagno;
		float iva=0.22;
		totale=totale+totale*iva;
		
		cout<<"Il prezzo di vendita di "<<importo<<" euro con perc. di guadagno al "<<percguadagno*100<<"%, l'IVA al 22% e "<<numerosconti<<" sconto/i e': "<<totale;
		
	}
	
	return 0;
}