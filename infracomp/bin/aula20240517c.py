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
    return(sum)

if __name__ == "__main__":
    num_steps = 10000000    # 10.000.000 (10e7)
    sums = 0.0
    step = 1.0/num_steps
    tic = time.time()
    sums = pi_naive(0, num_steps, step)
    tac = time.time()
    pi = step * sums
    print("Valor Pi: %.10f" %pi)
    print("Tempo Pi: %8f s" %(tac - tic))


print(sums)
print(pi)