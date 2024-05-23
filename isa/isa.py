"""libreria per interpretare argomenti da linea di comando"""
import argparse 
"""libreria per interagire con il sistema operativo"""
import sys 
"""libreria per gestire log"""
import logging

import math

class Operations():
    """
    Calcola metriche di errore tra predicted e expected values (MAE, MSE) 
    """
    def __init__ (self,
                  predicted: 'list[float]',
                  expected: 'list[float]',
                  metrics: str) -> None:
        self.predicted: 'list[float]' = predicted
        self.expected: 'list[float]' = expected
        self.metrics: str = metrics

        if not self._is_consistent():
            # print("Error: predicted and expected lists have different lengths")
            # logging.critical("Error: predicted and expected lists have different lengths")
            raise ValueError("Error: predicted and expected lists have different lengths")
            sys.exit(1)

    def _is_consistent(self) -> bool:
        return len(self.predicted) == len(self.expected)

    def _mae(self) -> float:
        """
        Mean Absolute Error
        """
        result: float = 0
        for i in range(0, len(self.predicted)):
            result += abs(self.predicted[i] - self.expected[i])
        return result / len(self.predicted)

    def _mae_zip(self) -> float:
        """
        Mean Absolute Error
        """
        result: float = 0
        for p, e in zip(self.predicted, self.expected):
            result += abs(p - e)
        return result / len(self.predicted)

    def _mae_map(self) -> float:
        """
        Mean Absolute Error
        """
        result: float = 0
        fn = lambda p, e : abs(p - e)
        result = sum( list(map(fn, self.predicted, self.expected)) )
        
        return result / len(self.predicted)   

    def _mse(self) -> float:
        """
        Mean Squared Error
        """
        result: float = 0
        for i in range(0, len(self.predicted)):
            result += (self.predicted[i] - self.expected[i])**2
        return result / len(self.predicted)
    
    def _rmse(self) -> float:
        """
        Root Mean Squared Error
        """
        return self._mse()**0.5

    def compute_metrics(self) -> float:
        """
        Calcola la metrica richiesta
        """
        if self.metrics == 'MAE':
            return self._mae()
        elif self.metrics == 'MSE':
            return self._mse()
        elif self.metrics == 'MAE_ZIP':
            return self._mae_zip()
        elif self.metrics == 'RMSE':
            return self._rmse()
        else:
            print("Error")
            return -1

def setup_parser() -> argparse.Namespace:
    """
    Funzione
    """
    parser = argparse.ArgumentParser(
                        prog='isa',
                        description='computes error metrics')

    parser.add_argument('--predicted',
                        type=float,
                        nargs='+',
                        required=True,
                        help='Predicted values')

    parser.add_argument('--expected',
                        type=float,
                        nargs='+',
                        required=True,
                        help='Expected values')

    parser.add_argument('--metrics',
                        type=str,
                        required=True,
                        help='Metrics to compute',
                        choices=['MAE','MSE','MAE_ZIP','RMSE'])
    
    return parser.parse_args()


def main(arguments):
    """
    1. interpretazione argomenti da linea di comando
       $ isa --predicted 1 2 3 --expected 1 2 4 --metrics MAE
    """

    print("Hello, World!")
   
    
    logging.basicConfig(level=logging.WARNING) #DEBUG, INFO, WARNING, ERROR, CRITICAL
    """
    DEBUG: dettagli completi, di solito utilizzato solo per il debug
    INFO: messaggi informativi che mostrano il funzionamento del programma
    WARNING: indicazioni di potenziali problemi nel programma
    ERROR: indicazioni di errori nel programma
    CRITICAL: indicazioni di errori gravi nel programma
    """

    logging.debug(arguments.predicted)
    # print(Arguments.predicted)
    logging.debug(arguments.expected)
    # print(Arguments.expected)
    logging.debug(arguments.metrics)
    # print(Arguments.metrics)

    #2. creazione oggetto Operations
    solver = Operations(arguments.predicted, arguments.expected, arguments.metrics)

    #3. calcolo metrica
    return solver.compute_metrics()
    

if __name__ == '__main__':
    result = main(setup_parser())
    print(result)

# Aggiungo un commento
