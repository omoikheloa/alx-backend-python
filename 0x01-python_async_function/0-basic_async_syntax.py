#!/usr/bin/env python3
'''The basics of async
An asynchronous coroutine that takes in an integer
argument (`max_delay`, with a default value of 10) named
`wait_random` that waits for a random delay between 0 and
`max_delay` and eventually returns it.

Using the `random` module.

'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random number of seconds
    '''
    random_val = random.uniform(0, max_delay)
    await asyncio.sleep(random_val)
    return random_val
