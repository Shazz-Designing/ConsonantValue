import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import solve

def test_solve():
    assert solve("zodiacs") == 54
    assert solve("strength") == 111
