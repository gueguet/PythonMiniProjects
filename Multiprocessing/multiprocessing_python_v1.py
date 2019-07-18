from multiprocessing import Process

def frist_test(my_num):
    print('yosh {}'.format(my_num))

if __name__ == "__main__":
    print("start")
    for i in range(100):
        # if you just have one argument, need a comma
        p = Process(target=frist_test, args=(i, ))
        p.start()

        # wait for the process to be completed
        # terminal mac --> check it with ps -ax | grep python
        # p.join()

"""
With p.join you are sure that the processes happened in order.
"""

