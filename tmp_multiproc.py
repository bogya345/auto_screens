import multiprocessing as multiproc
import threading

# class myThread1 (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print("Starting " + self.name)
#         worker1()
#         print("Exiting " + self.name)
# class myThread2 (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print("Starting " + self.name)
#         worker2()
#         print("Exiting " + self.name)

counter = 0

# manager = multiprocessing.Manager() 
# final_list = manager.list()

class myThread (threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func
    def run(self):
        print("Starting " + self.name)
        self.func()
        print("Exiting " + self.name)

def worker1():
    # lock.acquire()
    global counter
    for item in range(0,6):
        counter += 1
    # lock.release()

def worker2():
    # lock.acquire()
    global counter
    for item in range(0,5):
        counter += 1
    # lock.release()


if __name__ == '__main__':

    lock = multiproc.Lock()

    input_list_one = ['one', 'two', 'three', 'four', 'five']
    input_list_two = ['six', 'seven', 'eight', 'nine', 'ten']

    # process1 = multiproc.Process(target=worker1, args=[input_list_one, lock])
    # process2 = multiproc.Process(target=worker2, args=[input_list_two, lock])
    # process1.start()
    # process2.start()
    # process1.join()
    # process2.join()

    # thread1 = myThread1(1,'kek1',1)
    # thread2 = myThread2(2,'kek2',2)
    func1 = worker1
    func2 = worker2
    thread1 = myThread(func1)
    thread2 = myThread(func2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print ("Exiting Main Thread")

    print(counter)
    