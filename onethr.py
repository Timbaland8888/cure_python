#!/usr/bin/env python
#Arthuor:Timbaland
#DATE:2018-0629
#使用单线程执行循环

from time import  sleep,ctime
import _thread

# def loop0():
#     print('start loop 0 at:{}'.format(ctime()))
#     sleep(4)
#     print(' loop 0 done at:{}'.format(ctime()))
#
#
#
# def loop1():
#     print('start loop 1 at:{}'.format(ctime()))
#     sleep(2)
#     print(' loop 1 done at:{}'.format(ctime()))
#
#
# def main():
#     print("start at:{}".format(ctime()))
#     _thread.start_new(loop0,())
#     _thread.start_new(loop1,())
#     sleep(4)
#     print("all done at:{}".format(ctime()))
#
# if  __name__ == '__main__':
#     main()

loops = [4,2]
def loop(nloop,nsec,lock):
    print("start loop",nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'done at:',ctime())
    lock.release()


def main():
    print('starting at:',ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock =_thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    print(locks)
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))


    for i in nloops:
        while locks[i].locked():pass
    print( 'all DONE at:',ctime())


if __name__ == '__main__':
    main()
