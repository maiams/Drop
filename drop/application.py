# -*- coding: utf-8 -*-
import time


class Application(object):

    def __init__(self):
        self.log = "stress.txt"

    def run(self, callback):
        def wrapper(*args, **kwargs):
            start = time.time()
            body = callback(*args, **kwargs)
            end = time.time()
            time_to_run = str(end - start)

            return body

        return wrapper

    def __log(self, log):
        f = open(self.log)
