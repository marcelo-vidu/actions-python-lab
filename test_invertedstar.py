# test_invertedstar.py

import invertedstar

def test_invertedstar_5(capsys):
    invertedstar.invertedstar(5)
    captured = capsys.readouterr()
    assert captured.out == "*****\n ****\n  ***\n   **\n    *\n"

def test_invertedstar_3(capsys):
    invertedstar.invertedstar(3)
    captured = capsys.readouterr()
    assert captured.out == "***\n **\n  *\n"

def test_invertedstar_1(capsys):
    invertedstar.invertedstar(1)
    captured = capsys.readouterr()
    assert captured.out == "*\n"