
# EXEMPLO 3: COMUNICADOR PIPE

from multiprocessing import Process , Pipe

def worker(conn) :
    while True :
        item = conn.recv()
        if item == 'fim' :
            break
        print(item)

def master(conn) :
    conn.send(' Isto')
    conn.send(' esta')
    conn.send(' funcionando?')
    conn.send('fim')



if __name__ == '__main__' :
    a, b = Pipe()
    w = Process(target = worker, args = (a, ) )
    m = Process(target = master, args = (b, ) )
    w.start()
    m.start()
    w.join()
    m.join() 

