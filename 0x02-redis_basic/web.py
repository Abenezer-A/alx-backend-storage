#!/usr/bin/env python3

'''
method that implements an expiring web cache and tracker
'''

from typing import Callable
from functools import wraps
import redis
import requests


def requests_counter(method: Callable) -> Callable:
    """ Counts how many times a request has been made
    """
    r = redis.Redis()

@requests_counter
def get_page(url: str) -> str:
    """ obtains html content for a given site url and returns it.
    """
    resp = requests.get(url)
    return resp.
