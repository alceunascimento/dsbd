from multiprocessing import Pool
import time

PROCS = 6

def pi(args):
    start, end, step = args
    print("Start: " + str(start))
    print("End: " + str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i + 0.5) * step
        sum += 4.0 / (1.0 + x * x)
    return sum

tic = time.time()

if __name__ == "__main__":
    num_steps = 10000000
    step = 1.0 / num_steps
    proc_size = num_steps // PROCS
    
    with Pool(PROCS) as pool:
        results = pool.map(pi, [(i * proc_size, (i + 1) * proc_size, step) for i in range(PROCS)])
    
    total_sum = sum(results)
    toc = time.time()
    
    pi_value = step * total_sum
    
    print("Valor Pi: %.20f" % pi_value)
    print("Tempo Pi: %.8f s" % (toc - tic))
