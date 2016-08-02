# -*- coding: utf-8 -*-
import time

_fname = "test.log"

def _log(file, log):
    f = open(file, 'w')
    f.write(log)
    f.close()


def _read_log(file):
    f = open(file, 'r')
    content = f.read()
    f.close()
    return content


class Application(object):

    @staticmethod
    def run(callback):
        def wrapper(*args, **kwargs):
            start = time.time()
            body = callback(*args, **kwargs)
            end = time.time()
            time_to_run = str(end - start)
            _log(_fname, time_to_run)
            return body

        return wrapper

    @staticmethod
    def print_result(callback):
        def wrapper(*args, **kwargs):
            body = callback(*args, **kwargs)
            content = _read_log(_fname)
            print(content)
            return body

        return wrapper


