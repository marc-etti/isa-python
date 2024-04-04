# Contiene la descrizione testuale di cosa fa la mia applicazione
MD e LICENSE sono i due file comuni ad ogni progetto e stanno nella cartella base
poi avremo:
cartella riservata ai documenti "doc/"
cartella riservata ai sorgenti  "isa/"
cartella riservata ai test  "tests/"

Questo layout di organizzazione del progetto si chiama flat layout

pyproject.com è il file che dice come impacchettare la nostra applicazione (va chiamato proprio così)

comando tree per vedere la visualizzazione ad albero del nostro progetto

# Esempio di contenuto del file README.md

Isa è l'applicazione a linea di comando che date due liste di interi calcola alcune metriche.
    MAE Min Absolute Error
    MSE Min Square Error

Esempio:
l1=[1,2,3]
l2=[1,2,4]

MAE = 1 / len(l1) * somma( l1[i] - l2[i] )

(|1 - 1| + |2 - 2| + |3 - 4|) / 3

Vorrei chiamare la mia applicazione in questo modo:

    $ isa --predicted 1 2 3 --expected 1 2 4 --metrics MAE

# Master e Branch
