import time
def timer():
    while True:
        try:
            print("Stopwatch has started")
            start_time=time.time()
            while True:
                print("Time elapsed:",round(time.time()-start_time,0),'secs',end='\n')
                time.sleep(1)
        except KeyboardInterrupt:
            print("Timer has stopped")
            end_time=time.time()
            timee = round(end_time-start_time,2)
            break
timer()