from pythonCICD.app import app

def test_health_check():
    response = app.test_client().get('/health_check')
    assert response.status_code == 200
    assert response.data == b"Successul API health check!"

    print(response.status_code, response.data)

if __name__ == "__main__":
    test_health_check()