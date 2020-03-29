"""
Additional types for checking
"""

# Copyright (C) 2020 The Psycopg Team

from typing import Any, Callable, Mapping, Sequence, Tuple, Union

EncodeFunc = Callable[[str], Tuple[bytes, int]]
DecodeFunc = Callable[[bytes], Tuple[str, int]]

Query = Union[str, bytes]
Params = Union[Sequence[Any], Mapping[str, Any]]
