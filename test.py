# coding: utf-8
from __future__ import print_function, unicode_literals, absolute_import

import types
import inspect

import lib
import testlib


ids = {}
for k, v in testlib.__dict__.items():
    if isinstance(v, types.FunctionType) or inspect.isclass(v):
        ids[k] = id(v)

lib.force_reload(testlib)

for k, v in testlib.__dict__.items():
    if isinstance(v, types.FunctionType) or inspect.isclass(v):
        ids[k] = id(v)

