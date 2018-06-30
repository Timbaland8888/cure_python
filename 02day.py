#!/usr/bin/env  python

from threading import Thread
from  time import sleep ,ctime

loops = [4,2]
def loop(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop ',nloop,'done at:',ctime())



def main():
    print('staring at:',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    print('all done ')


if __name__ == '__main__':
    main()


