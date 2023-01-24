from src.store_data import store_data
from src.download_data import get_data

def test_store_data():
    key = 'test_key'
    data = b'Test data'
    expected_response = {'message': 'Data stored successfully in Dropbox'}
    response = store_data(key, data)
    assert response == expected_response


def test_download_data():
    key = 'test_key'
    expected_response = f"filename:{key} successfully downloaded"
    response = get_data(key)
    assert response == expected_response