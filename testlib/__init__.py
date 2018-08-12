# coding: utf-8
from __future__ import print_function, unicode_literals, absolute_import

from .libsrc1 import *
from .libsrc2 import lib2_f2, instance1
from testlib.libsrc3 import lib3_f1 as lib31
import libsrc4 as src4

from .testsub import *


def test1():
    print('test1')


def test2():
    print('test2')
