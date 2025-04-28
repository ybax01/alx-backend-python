#!/usr/bin/env python3
"""
Task 4
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random



async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Alternate function to the older wait_n function
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
