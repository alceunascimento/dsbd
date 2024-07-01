# MULTIPROCESSOS EM PYTHON

# setup
from multiprocessing import Process
import time


# script 

def pi_naive(start, end, step):
    print('Start: ', str(start))
    print('End: ', str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i + 0.5) * step
        sum = sum + 4.0/(1.0 + x*x)
    print(sum)


if __name__ == "__main__":
    # parametros
    n = 1000000
    procs = 4
    id_ini = (n // procs)
    
    id_fim = (n // procs) - 1 * (id_ini + 1)
    i = 1.0 / n

    # Cria e inicia cada processo
    for i in range(procs):
        p = Process(target=pi_naive, args=(id_ini, id_fim, i))
        procs.append(p)
        p.start()

    # Aguarda a conclusão de todos os processos
    for p in procs:
        p.join()


    
    tac = time.time()


    print("Valor Pi: %.10f" %pi)
    print("Tempo Pi: %8f s" %(tac - tic))





