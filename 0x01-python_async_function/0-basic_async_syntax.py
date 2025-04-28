#!/usr/bin/env python3
"""
The basics of async
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random time with a set maximum
    """
    waiting_time = random.uniform(0,max_delay)
    await asyncio.sleep(waiting_time)
    return waiting_time
