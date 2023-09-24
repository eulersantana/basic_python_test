import pytest
from main import soma, subtracao


def test_soma():
   assert 4 == soma(2, 2)

def test_subtracao():
   assert 0 == subtracao(2, 2)