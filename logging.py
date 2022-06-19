import logging
import sys, os
import traceback
import time

import random
logging.basicConfig(level=logging.DEBUG,
                    filename='logs_example.log',
                    filemode='w',
                    format='NEW LOG - %(asctime)s - %(levelname)s: %(message)s')
class Timers:
    def timer(self):
        self.a = random.randint(1, 15)
        print("Time = ", self.a)
class Slaves(Timers):
    def slave(self):
        b = 0
        try:
            if(b<=self.a):
                print("I`m working")
                b+=1
                time.sleep(1)
        except BaseException as error:
            print("Error During Getting Time")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.critical(type(error).__name__ + ": " + str(error) + '::' + repr(traceback.format_tb(exc_tb)))


worker = Slaves()
worker.timer()
worker.slave()

