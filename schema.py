"""Helper decorator to measure time costs and memery costs"""

__author__= "Xuan Yang (jumpthepig@gmail.com)"


from functools import wraps
import time
import resource


def time_it(func):
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
        return _result
    return inner
