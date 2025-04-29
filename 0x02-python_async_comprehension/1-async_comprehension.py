#!/usr/bin/env python3
"""1. Async Comprehensions"""

from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension from async_generator."""
    return [i async for i in async_generator()]
