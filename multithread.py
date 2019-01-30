# -*- coding:utf-8 -*- 

from multiprocessing import Process, Queue
import urllib
import os, random, time
import threading

download_count = 1

def readurl(q):
    count = 1
    print "now queue size : "+ str(q.qsize())
    with open("raw_data/neutral/urls_neutral.txt",'r') as f:
        for line in f:
            q.put(line)
            print "read "+str(count)+" ulr "
            # time.sleep(random.random())
            count +=1

def downurl(q ,lock):
    global download_count
    folder = 'pics/'

    print str(q.qsize())
    print "thread %s is running..." %threading.current_thread().name
    lock.acquire()
    try:
        url = q.get()
        print str(download_count)+" : "+url
        filename = folder + str(download_count)+".jpg"
        print filename
        try:
            # urlretrieve 实现机制, 对于一个网络不可达的情况快速处理
            _, header = urllib.urlretrieve(url,filename)
            print "download "+str(download_count)+".jpg"
        except Exception as e:
            print "exception : e : "+str(e)
            print "can not download "+str(download_count)+".jpg"
        download_count+=1
    finally:
        lock.release()

if __name__ == "__main__":
    q = Queue()
    readurl(q)
    lock = threading.Lock()
    for i in range(5):
        t = threading.Thread(target = downurl, args=(q,lock))
        t.start()
        t.join()
