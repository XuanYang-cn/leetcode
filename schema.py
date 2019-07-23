"""Helper decorator to measure time costs and memery costs"""

__author__= "Xuan Yang (jumpthepig@gmail.com)"


from functools import wraps
import time
import resource
import os


def time_it_old(func):
    @wraps(func)
    def inner(*args):
        date = ('{}-{}-{} {}:{}:{}').format(*time.localtime(time.time()))
        t0 = time.perf_counter_ns()
        _result = func(*args)
        elapsed = (time.perf_counter_ns() - t0)/1000
        if _result:
            print(f'[{date}]: [{elapsed:0.4f}ms]{func.__name__} -> {_result}')
        else:
            print(f'[{date}]: [{elapsed:0.4f}ms]{func.__name__}')
        return _result
    return inner


def mem_time_resource(func):
    @wraps(func)
    def inner(*args):
        date = ('{}-{}-{} {}:{}:{}').format(*time.localtime(time.time()))
        rss_before, shared_before, unshared_before = resource.getrusage(resource.RUSAGE_SELF)[2:5]
        t_before = resource.getrusage(resource.RUSAGE_SELF).ru_utime

        _result = func(*args)

        t_after = resource.getrusage(resource.RUSAGE_SELF).ru_utime
        rss_after, shared_after, unshared_after = resource.getrusage(resource.RUSAGE_SELF)[2:5]

        fomater = f"mem before:{rss_before:7}, mem after:{rss_after:7}, time before:{t_before:7.8f}, time after:{t_after:7.8f}"
        print(fomater)
        if _result:
            pass
            #print(f'[{date}]: [{elapsed:0.4f}ms]{func.__name__} -> {_result}')
        else:
            pass
            #print(f'[{date}]: [{elapsed:0.4f}ms]{func.__name__}')


def elapsed_since(start):
    elapsed = time.perf_counter_ns() - start

    return elapsed/1000

def get_process_memory():
    process = psutil.Process(os.getpid())
    mi = process.memory_info()

    return mi.rss, mi.vms, mi.shared

def format_bytes(b):
    if abs(b) < 1000:
        return str(b) + "b"
    elif abs(b) < 1e6:
        return str(round(b/1e3, 2)) + "KB"
    elif abs(b) < 1e9:
        return str(round(b/1e6, 2)) + "MB"
    else:
        return str(round(b/1e9, 2)) + "GB"


def time_it(func):
    @wraps(func)
    def inner(*args, **kwargs):
        rss_b, vms_b, sm_b = get_process_memory()
        print(rss_b)
        t0 = time.perf_counter_ns()

        _result = func(*args, **kwargs)

        elapsed = elapsed_since(t0)
        rss_a, vms_a, sm_a = get_process_memory()
        print(rss_a)
        if _result is not None:
            print(f"time: {elapsed:0.4f}ms | RSS: {} | VMS: {} | SHR: {} | [{func.__name__}] -> {_result}")
            #print(f'[{elapsed}]{func.__name__} -> {_result}')
        else:
            #print(f'[{date}]: [{elapsed}]{func.__name__}')
            print(f"time: {elapsed:0.4f}ms | RSS: {} | VMS: {} | SHR: {} | [{func.__name__}]")
        return _result
    return inner
