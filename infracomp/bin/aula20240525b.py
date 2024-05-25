# EXERCICIO 4
"""
Transforme o programa Pi em paralelo utilizando PIPES.
Vamos precisar:
1. Criar um pipe e atribuir a duas variáveis
2. Enviar uma ponta do pipe para todos os processos
3. Os processos filho irão chamar send()
4. O processo master irá chamar recv()

CONTROLE O ACESSO AOS RECURSO E EVITE ERROS DE CORRIDA COM LOCKS
"""



# setup
from multiprocessing import Process, Pipe
import time


pi_value = 3.14159265358979323846264338327950288419716939937510


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
    for i in range(PROCS):
        # trabalhador unitario
        worker = Process(target = pi, # chama a funcao master
                        args=(i*proc_size, (i+1)*proc_size - 1, step, a, ) # define os argumentos da funcao master
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
