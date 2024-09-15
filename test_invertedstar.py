# test_invertedstar.py

import invertedstar
import pytest

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
    # test_invertedstar.py

    import azure.functions as func

    def test_invertedstar_5():
        result = invertedstar.invertedstar(5)
        expected = "*****\n ****\n  ***\n   **\n    *"
        assert result == expected

    def test_invertedstar_3():
        result = invertedstar.invertedstar(3)
        expected = "***\n **\n  *"
        assert result == expected

    def test_invertedstar_1():
        result = invertedstar.invertedstar(1)
        expected = "*"
        assert result == expected

    def test_invertedstar_0():
        result = invertedstar.invertedstar(0)
        expected = ""
        assert result == expected

    def test_main_valid_request():
        req = func.HttpRequest(
            method='GET',
            url='/api/invertedstar',
            params={'n': '5'},
            body=None
        )
        response = invertedstar.main(req)
        expected = "*****\n ****\n  ***\n   **\n    *"
        assert response.status_code == 200
        assert response.get_body().decode() == expected

    def test_main_invalid_request_non_integer():
        req = func.HttpRequest(
            method='GET',
            url='/api/invertedstar',
            params={'n': 'abc'},
            body=None
        )
        response = invertedstar.main(req)
        assert response.status_code == 400
        assert response.get_body().decode() == "Please provide a valid positive integer for the number of lines. Example: ?n=5"

    def test_main_invalid_request_negative_integer():
        req = func.HttpRequest(
            method='GET',
            url='/api/invertedstar',
            params={'n': '-5'},
            body=None
        )
        response = invertedstar.main(req)
        assert response.status_code == 400
        assert response.get_body().decode() == "Please provide a valid positive integer for the number of lines. Example: ?n=5"

    def test_main_invalid_request_missing_param():
        req = func.HttpRequest(
            method='GET',
            url='/api/invertedstar',
            params={},
            body=None
        )
        response = invertedstar.main(req)
        assert response.status_code == 400
        assert response.get_body().decode() == "Please provide a valid positive integer for the number of lines. Example: ?n=5"