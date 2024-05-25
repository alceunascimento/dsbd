# EXERCICIO 4
"""
Transforme o programa Pi em paralelo utilizando PIPES.
Vamos precisar:
1. Criar um pipe e atribuir a duas variáveis
2. Enviar uma ponta do pipe para todos os processos
3. Os processos filho irão chamar send()
4. O processo master irá chamar recv()

CONTROLE O ACESSO AOS RECURSO E EVITE ERROS DE CORRIDA COM LOCKS

Transforme o programa Pi em paralelo usando PIPES com locks!
Agora vamos utilizar locks para que nosso programa seja
multiprocess-safe
Vamos precisar:
1. Criar um lock
2. Enviar o lock como parâmetro
3. Antes de inserir no pipe, vamos usar o lock….. “ with lock:"

"""


# Exemplo
"""
import multiprocessing
import sys

def trabA(lock, stream):
    with lock:
        stream.write('Trabalhador 1 imprimindo\n')

def trabB(lock, stream):
    lock.acquire()
    stream.write('Trabalhador 2 imprimindo\n')
    lock.release()

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    w1 = multiprocessing.Process(target=trabA, args=(sys.stdout, ))
    w2 = multiprocessing.Process(target=trabB, args=(sys.stdout, ))
    w1.start()
    w2.start()
    w1.join()
    w2.join()
"""


# setup
from multiprocessing import Process, Pipe, Lock
import time


pi_value = 3.14159265358979323846264338327950288419716939937510


# definir a função de pi (como master)
def pi(lk, start, end, step, sums):
    print ("Start: ", str(start))
    print ("End: ", str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i + 0.5) * step
        sum = sum + 4.0 / (1.0 + x * x)
    with lk:
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
    lock = Lock()
    for i in range(PROCS):
        # trabalhador unitario
        worker = Process(target = pi, # chama a funcao master
                        args=(lock, i*proc_size, (i+1)*proc_size - 1, step, a, ) # define os argumentos da funcao master
                        )
        workers.append(worker) # append a lista de trabalhadores
    
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
