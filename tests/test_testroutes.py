import src.view as testapp

def test_Home():
    response = testapp.view.test_client().get('/')
    assert b"hello-world" in response.data
    assert response.status_code == 200