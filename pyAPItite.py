import requests

def generate_tests(swagger_url, base_url, output_file):
    # fetch swagger doc
    response = requests.get(swagger_url)
    response.raise_for_status()
    swagger = response.json()
    
    paths = swagger.get("paths", {})
    test_functions = []

    # inspect doc for GET methods
    for path, methods in paths.items():
        if "get" in methods:
            # create test/ function names from swagger endpoint 
            test_name = "test_get_" + path.strip("/").replace("/", "_").replace("{", "").replace("}", "")
            full_url = base_url + path

            # write the tests, yo
            function_body = f"""
def {test_name}():
    response = requests.get(f"{full_url}")
    # Assert that the GET request returns a 200 OK response
    assert response.status_code == 200, f"GET {full_url} returned {{response.status_code}}"
"""
            test_functions.append(function_body)

    # write tests to file
    with open(output_file, "w") as f:
        f.write("import requests\n")
        f.write("# add query params\n")

        for func in test_functions:
            f.write(func)
            f.write("\n")

if __name__ == "__main__":
    # necessary vars
    swagger_url = "https://fakerestapi.azurewebsites.net/swagger/v1/swagger.json"
    base_url = "https://fakerestapi.azurewebsites.net"
    output_file = "test_api.py"
    
    generate_tests(swagger_url, base_url, output_file)
    print(f"API tests generated in {output_file}")

