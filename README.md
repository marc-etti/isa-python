# ISA
## ISA v0.1
`Isa` è l'applicazione a linea di comando che date due liste di interi calcola alcune metriche.
- MAE Min Absolute Error
- MSE Min Square Error
- RMSE Root Mean Square Error

## Installazione:
```bash
$ python3 pip install isa
```

## Esempio
l1=[1,2,3]
l2=[1,2,4]

MAE = 1 / len(l1) * somma( l1[i] - l2[i] )

(|1 - 1| + |2 - 2| + |3 - 4|) / 3

### Chiamata dell'applicazione

    $ isa --predicted 1 2 3 --expected 1 2 4 --metrics MAE

## Utilizzo
```bash
usage: isa [-h] --predicted PREDICTED [PREDICTED ...] --expected EXPECTED [EXPECTED ...] --metrics {MAE,MSE}

computes error metrics

options:
  -h, --help            show this help message and exit
  --predicted PREDICTED [PREDICTED ...]
                        Predicted values
  --expected EXPECTED [EXPECTED ...]
                        Expected values
  --metrics {MAE,MSE}   Metrics to compute
```

