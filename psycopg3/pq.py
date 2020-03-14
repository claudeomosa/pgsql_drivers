"""
psycopg3 libpq wrapper

This package exposes the libpq functionalities as Python objects and functions.

The real implementation (the binding to the C library) is
implementation-dependant but all the implementations share the same interface.
"""

# Copyright (C) 2020 The Psycopg Team

from .pq_enums import ConnStatus

from . import pq_ctypes as pq_module

PGconn = pq_module.PGconn

__all__ = ("ConnStatus", "PGconn")