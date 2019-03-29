import data
import hashing
import logic
import server
import threading
import time

cycle_interval = 15

def go():
    #hosting server
    hosting_thread = threading.Thread(target=hostthread, args=() )
    hosting_thread.daemon = True
    hosting_thread.start()

    #other activities
    logic_thread = threading.Thread(target=logicthread, args=())
    logic_thread.daemon = True
    logic_thread.start()

    hash_thread = threading.Thread(target=hashthread, args=())
    hash_thread.daemon = True
    #hash_thread.start()

def hostthread():
    server.serve()

def hashthread():
    hashing.hash_thread()

def logicthread():
    s = time.time()
    while True:
        if time.time() - s > cycle_interval:
            logic.logic_cycle()
            s = time.time()

def init():
    data.try_generate_identity()

if __name__ == "__main__":
   go()
   k=0
   while True:
       k=0
