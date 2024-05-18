# MULTIPROCESSOS EM PYTHON

# setup
from multiprocessing import Process
import time

start_time = time.time()  

# script 

def f(name, id):
    print('hello, sou', name, id)

if __name__ == '__main__':
    procs = []
    for i in range(20):
       p = Process(target=f, args=('bob filho', i, ))
       procs.append(p)

    print('hello, sou', 'bob pai')
    for i in range(20):
        procs[i].start()
    for i in range(20):
        procs[i].join()



end_time = time.time()  # Registra o tempo de término
print(f"Tempo de execução: {end_time - start_time:.4f} segundos")