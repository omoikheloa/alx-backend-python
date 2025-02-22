#!/usr/bin/env python3
''' Computes run time for four parallel comprehensions
'''

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Computes run time
    '''
    i = perf_counter()
    task = [asyncio.create_task(async_comprehension()) for x in range(4)]
    await asyncio.gather(*task)
    elapsed = perf_counter() - i
    return elapsed
