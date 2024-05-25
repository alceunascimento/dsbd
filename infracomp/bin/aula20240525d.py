# EXERCICIO

"""
Transforme o programa Pi em paralelo usando QUEUEs.
Vamos precisar:
1. Substituir Pipe por Queue
2. Remover os Locks
3. Utilizar os métodos put/get invés de send/recv
"""

"""

from multiprocessing import Process, current_process
import itertools

##  itertools.count(start=0, step=1) : Make an iterator that returns evenly spaced values starting with number start.


ITEMS = Queue()
for i in [1, 2, 3, 4, 5, 6, 'end' , 'end' , 'end' ] :
    ITEMS.put(i)

def worker(items) :
    for i in itertools.count() :
        item = items.get()
        if item == 'end':
            break
    print(current_process().name, "processed %i items . " %i)

if __name__ == "__main__" :
    workers = [ Process (target = worker, args = (ITEMS, ) ) for i in range (3) ]
    for worker in workers :
        worker.start()
    for worker in workers :
        worker.join()
    print("ITEMS after all workers finished : " , ITEMS.qsize())

"""



# setup
from multiprocessing import Process, Pipe, current_process
import itertools
import time


pi_value = 3.14159265358979323846264338327950288419716939937510



PROCS = 2
sums = Queue()



# definir a função de pi (como master)
def pi(start, end, step, sums):
    print ("Start: ", str(start))
    print ("End: ", str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i + 0.5) * step
        sum = sum + 4.0 / (1.0 + x * x)
    sums.send(sum)


tic = time.time()

# Implementa as funções
if __name__ == '__main__':
    PROCS = 4 # define o numero de processos
    a,b = Pipe() # Estabelece o Pipe
    num_steps = 10000000  # número total de termos na série
    sum = 0.0  # valor inicial 
    step = 1.0/num_steps
    proc_size = num_steps // PROCS
    n_processes = 2  # número de processos para paralelizar


    # Criando e iniciando os processos worker
    workers = []  # listas de trabalhadores
    worker = [ Process(target = pi, # chama a funcao master
                        args=(ITEMS, ) # define os argumentos da funcao master
                        ) for i in range (3) ]
    
    # Inicia os processos
    for worker in workers:
        worker.start()

    # Aguarda o término dos processos
    for worker in workers:
        worker.join()

    #
    for i in range(PROCS):
        sum += b.recv()
    pi = step * sum

tac = time.time()

print ("Valor Pi: %.20f" %pi)
print ("Erro Pi: %.20f" %(pi_value - pi))
print ("Tempo: %.8f s" %(tac-tic))

