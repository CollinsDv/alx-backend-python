#!/usr/bin/env python3
"""module: 3-tasks

objectives
----------
Import wait_random

Write a function
    (do not create an async function, use the regular function syntax)
task_wait_random that takes an integer max_delay and returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('')


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio task for wait_random with the given max_delay."""
    return asyncio.create_task(wait_random(max_delay))
