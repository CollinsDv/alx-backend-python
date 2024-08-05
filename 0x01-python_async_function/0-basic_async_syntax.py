#!/usr/bin/env python3
"""module 0-basic_async_function
"""
import random
import asyncio
# Write an asynchronous coroutine that takes in an integer argument,
#   - (max_delay,default value of 10)
# named wait_random that waits for a random delay between 0 and max_delay
#   - (included and float value)
# seconds and eventually returns it.

# Use the random module.


async def wait_random(max_delay: int = 10) -> float:
    """waits on random delay
    Args:
        max_delay (int) -> upper bound for delay operation
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
