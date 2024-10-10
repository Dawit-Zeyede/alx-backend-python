#!/usr/bin/env python3
'''
Safe_first_element(lst).
'''
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    ''' Returs the first element if present or None
    '''
    if lst:
        return lst[0]
    else:
        return None
