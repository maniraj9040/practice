import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main&amp;amp;nbsp; &amp;amp;nbsp; : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main&amp;amp;nbsp; &amp;amp;nbsp; : before running thread")
    x.start()
    logging.info("Main&amp;amp;nbsp; &amp;amp;nbsp; : wait for the thread to finish")
    x.join()
    logging.info("Main&amp;amp;nbsp; &amp;amp;nbsp; : all done")