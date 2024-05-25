"""
EXERCÍCIO
Transforme o programa Pi em paralelo usando (VALUE ou ARRAY)!
Vamos precisar:
1. Criar uma variável Value, e envia-la a todos os processos filho.
2. Cada processo filho calcula sua parcela.
3. Ao final do cálculo, cada filho obtém o lock e atualiza a variável
compartilhada.
"""

from multiprocessing import Process, Value
import time

PROCS = 2

def pi(val, start, end, step,sums):
    print("Start: " + str(start))
    print("End: " + str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    with val.get_lock():
            val.value += sum


tic = time.time()

if __name__ == "__main__":
    num_steps = 100000000
    step = 1.0/num_steps
    proc_size = num_steps / PROCS
    workers = []
    v = Value('d', 0, lock=True)
    
    for i in range(PROCS):
        worker = Process(target = pi,
                        args =(v, i*proc_size, (i+1)*proc_size-1,step, sums)
                        )
        workers.append(worker)
    
    for worker in workers :
        worker.start()
    
    for worker in workers :
        worker.join()

    toc = time.time()

    pi = step * v.value
    
    print("Valor Pi: %.20f" %pi)
    print("Tempo Pi: %.8f s" %(toc-tic)