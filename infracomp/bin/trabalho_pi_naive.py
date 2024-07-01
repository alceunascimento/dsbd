from multiprocessing import Process, Manager
import time

def pi_naive(start, end, step, result, index):
    sum_part = 0.0
    for i in range(start, end):
        x = (i + 0.5) * step
        sum_part += 4.0 / (1.0 + x*x)
    result[index] = sum_part


tic = time.time()

if __name__ == "__main__":
    n = 10000000
    procs = 6
    step = 1.0 / n
    results = Manager().list([0]*procs)  # lista compartilhada para armazenar resultados

    processes = []

    # Cria e inicia cada processo
    for i in range(procs):
        start = i * (n // procs)
        if i == procs - 1:
            end = n  # assegura que o último processo pegue o restante
        else:
            end = start + (n // procs)
        p = Process(target=pi_naive, args=(start, end, step, results, i))
        processes.append(p)
        p.start()
    # Aguarda a conclusão de todos os processos
    for p in processes:
        p.join()

    # Imprimir os valores de cada processo
    for index, value in enumerate(results):
        print(f"Resultado do processo {index}: {value:.10f}")

    print(f'Soma dos resultados {sum(results)}')
    
    pi = sum(results) * step  # calcula o valor final de pi
    print("Valor de Pi: %.15f" % pi)

    tac = time.time()
    print("Tempo Pi: %8f s" % (tac - tic))

