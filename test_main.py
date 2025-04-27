# test_main.py
import main

def test_hello_http():
    response = main.hello_http(None)
    assert response == "Hello World!!!"
