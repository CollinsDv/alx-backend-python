#!/usr/bin/env python3
"""module: 2-measure_runtime

objectives
----------
import wait_n

Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time
"""
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """calculates execution time for function wait_n"""
    startTime = time.time()

    await wait_n(n, max_delay)

    return (time.time() - startTime) / n
