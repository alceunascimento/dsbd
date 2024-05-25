from multiprocessing import Pool

def func(val):
    return val*val

if __name__ == '__main__':
    itens = [1, 2, 3]
    p = Pool(8) # Cria um conjunto de 8 trabalhadores!
    resultado = p.map(func, itens)
    print(resultado)
    p.close()
    p.join() 