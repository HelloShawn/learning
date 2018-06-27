from multiprocessing import Process, Manager, Pool, Queue
import time,os,random

def write(q):
    for value in ['A','B','C','D','E','F','G','H']:
        print('put %s to queue...'%value)
        q.put(value)
        # time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print('get %s from queue...'%value)
            # time.sleep(random.random())
        else:
            break

if __name__=="__main__":
    q = Manager().Queue()
    po=Pool(5)
    #pw = Process(target=write,args=(q,))
    #pr = Process(target=read,args=(q,))
    # po.apply(write,(q,))
    # po.apply(read,(q,))#阻塞方式
    po.apply_async(write, (q,))
    po.apply_async(read, (q,))#非阻塞方式
    #pw.start()
    #pw.join()
    #pr.start()
    #pr.join()
    po.close()
    po.join()
    print('')
    print('all data is wrote and read')
