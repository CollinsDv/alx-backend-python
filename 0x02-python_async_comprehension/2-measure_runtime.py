#!/usr/bin/env python3
"""module: 2-measure_runtime.py"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measures the total runtime of executing async_comprehension
    four times in parallel."""
    start_time = time.perf_counter()

    # Run async_comprehension four times concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    total_runtime = time.perf_counter() - start_time
    return total_runtime
