import requests
# add query params
id = 1
idBook = 1

def test_get_api_v1_Activities():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Activities")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Activities returned {response.status_code}"


def test_get_api_v1_Activities_id():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Activities/{id}")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Activities/{id} returned {response.status_code}"


def test_get_api_v1_Authors():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Authors")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Authors returned {response.status_code}"


def test_get_api_v1_Authors_authors_books_idBook():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Authors/authors/books/{idBook}")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Authors/authors/books/{idBook} returned {response.status_code}"


def test_get_api_v1_Authors_id():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Authors/{id}")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Authors/{id} returned {response.status_code}"


def test_get_api_v1_Books():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Books")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Books returned {response.status_code}"


def test_get_api_v1_Books_id():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Books/{id}")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Books/{id} returned {response.status_code}"


def test_get_api_v1_CoverPhotos():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos returned {response.status_code}"


def test_get_api_v1_CoverPhotos_books_covers_idBook():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/books/covers/{idBook}")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/books/covers/{idBook} returned {response.status_code}"


def test_get_api_v1_CoverPhotos_id():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/{id}")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/{id} returned {response.status_code}"


def test_get_api_v1_Users():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Users")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Users returned {response.status_code}"


def test_get_api_v1_Users_id():
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Users/{id}")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET https://fakerestapi.azurewebsites.net/api/v1/Users/{id} returned {response.status_code}"

