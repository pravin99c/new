import threading
import time
a=1
  
def print_cube(name):
    """
    function to print cube of given global variable
    """
    global a
    for i in range(50):
        a += 1
        time.sleep(0.5)
        print("call Tread : {} Cube: {}".format(name,a * a * a))
 
  
def main():
    # creating thread
    t1 = threading.Thread(target=print_cube, args=(1,))
    t2 = threading.Thread(target=print_cube, args=(2,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")

if __name__ == "__main__":
    main()
    print("Done all task")