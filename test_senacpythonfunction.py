import azure.functions as func
import pytest
import senacpythonfunction

def test_main_valid_request():
    req = func.HttpRequest(
        method='GET',
        url='/api/hello',
        params={},
        body=b'{"name": "Jane"}'
    )
    response = senacpythonfunction.main(req)
    assert response.status_code == 200
    assert response.get_body().decode() == "Hello, Jane!"

def test_main_invalid_request_no_name():
    req = func.HttpRequest(
        method='GET',
        url='/api/hello',
        params={},
        body=None
    )
    response = senacpythonfunction.main(req)
    assert response.status_code == 400
    assert response.get_body().decode() == "Please pass a name on the query string or in the request body"

def test_main_invalid_request_empty_body():
    req = func.HttpRequest(
        method='POST',
        url='/api/hello',
        params={},
        body=b'{}'
    )
    response = senacpythonfunction.main(req)
    assert response.status_code == 400
    assert response.get_body().decode() == "Please pass a name on the query string or in the request body"

def test_main_invalid_request_invalid_json():
    req = func.HttpRequest(
        method='POST',
        url='/api/hello',
        params={},
        body=b'{invalid_json}'
    )
    response = senacpythonfunction.main(req)
    assert response.status_code == 400
    assert response.get_body().decode() == "Please pass a name on the query string or in the request body"