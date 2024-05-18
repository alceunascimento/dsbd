# MULTIPROCESSOS EM PYTHON

# setup
from multiprocessing import Process
import time

start_time = time.time()  

# script 

def f(name):
    print('helo, sou', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob filho', ))
    p.start()
    p.join()



end_time = time.time()  # Registra o tempo de término
print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
