 
'''
    import pdb
    s = '2'
    n = int(s)
    pdb.set_trace()  #程序运行到这里会自动暂停
    print(10/n)

from multiprocessing import Process
import os
def run_proc(name):
   print('Run child process %s (%s)...' %(name, os.getpid()))

if __name__ == '__main__':
   print('Parent process %s. '% os.getpid())
   p = Process(target=run_proc, args=('test',))
   print('Child process will start.')
   p.start()
   p.join()
   print('Child process end.')
'''

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')