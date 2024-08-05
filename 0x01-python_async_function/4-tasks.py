#!/usr/bin/env python3
"""module: 4-tasks

ensure the defined async func in file 1 is callable
"""
import asyncio
wait_random = __import__(
                         '0-basic_async_syntax').wait_random
from typing import List


async def task_wait_random(n: int, max_delay: int) -> List[float]:
    """spans wait_random and returns list of return value
    Args:
        n(int) -> number of iterations
        max_delay(int) -> maximum delay time

    Return:
        List of sorted delay values
    """
    delayList = []
    delayList = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n)))
    return sorted(delayList)
