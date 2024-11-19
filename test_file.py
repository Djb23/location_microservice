import requests


baseURL = "http://127.0.0.1:5000"

def test_search_location():
    print("Testing Search:")
    query = "Wash"
    response = requests.get(f"{baseURL}/search", params={"query": query})
    print(f"Search Response: {response.json()}")


def test_add_location():
    print("Testing Add Location:")
    location_data = {
        "city": "Brooklyn",
        "state": "NY"
    }
    headers = {"Admin-Password": "abc123"}
    response = requests.post(f"{baseURL}/add_location", json=location_data, headers=headers)
    print(f"Add Location Response: {response.json()}")

def test_remove_location():
    print("Testing Remove Location:")
    headers = {"Admin-Password": "abc123"}
    location_to_remove = {
        "city": "Washington",
        "state": "DK"
    }
    response = requests.delete(f"{baseURL}/remove_location", headers=headers, json=location_to_remove)
    print(f"Remove Location Response: {response.json()}")


if __name__ == "__main__":
    test_search_location()
    test_add_location()
    test_remove_location()

