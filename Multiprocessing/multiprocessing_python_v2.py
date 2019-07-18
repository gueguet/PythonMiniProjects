import os, time
from multiprocessing import Process, current_process

def square(my_num):
    result = my_num * my_num

    process_id = os.getpid()
    process_name = current_process().name

    print("process id {}, process name {}".format(process_id, process_name))
    print("result : {}".format(result))

if __name__ == '__main__':

    processes = []
    numbers = [1,2,3,4]

    for number in numbers:

        start = time.time()

        p = Process(target=square, args=(number,))
        processes.append(p)
        p.start()
        p.join()

    end = time.time()

    print("Execution time {}".format(str(end-start)))
