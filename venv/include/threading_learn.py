import threading
from time import ctime,sleep

def eating(func):
    for i in range(2):
        print("我在吃。。。emmm %s. %s"%(func,ctime()))
        sleep(1)
def playing_game(func):
    for i in range(2):
        print("我在玩....ooohh%s. %s"%(func,ctime()))
        sleep(1)

threads = []#创建来threads数组
t1 = threading.Thread(target=eating,args=("chips",))
threads.append(t1)
t2 = threading.Thread(target=playing_game,args=("吃鸡",))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()#在子线程完成之前，父线程会被阻塞

    print("finish! %s"%ctime())
"""子线程启动后，父线程会跟着执行下去，当父线程完成最后一条语句的时候，由于子线程是父线程的守护线程所以它会守护父线程，什么时候父线程结束，子线程就跟着一起结束，不管子线程有没有执行完"""