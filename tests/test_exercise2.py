import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_clamp():
    assert clamp(15, 1, 10) == 10


# bug report 2
def test_r2_is_passing():
    assert is_passing(5) == True
