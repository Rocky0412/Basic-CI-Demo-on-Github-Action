from app import Substract, Sum
import sys
import os



def test_Sum():
    assert Sum(5, 6) == 11

def test_Substract():
    assert Substract(6 , 7) == -1