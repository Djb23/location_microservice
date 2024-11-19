from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
locations_file = 'locations.json'
admin_pass = "abc123"

def load_locations():
    if os.path.exists(locations_file):
        with open(locations_file, 'r') as file:
            return json.load(file)
    return []

def save_locations(locations):
    with open(locations_file, 'w') as file:
        json.dump(locations, file, indent=5)

# Search locations based on a partial or full input
@app.route('/search', methods=['GET'])
def search_locations():
    query = request.args.get('query', '')
    locations = load_locations()
    matches = [f"{loc['city']}, {loc['state']}" for loc in locations if query.lower() in loc['city'].lower()]
    return jsonify(matches)

# Add a new location with password
@app.route('/add_location', methods=['POST'])
def add_location():
    admin_password = request.headers.get('Admin-Password')

    if admin_password != admin_pass:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    city_name = data.get("city")
    state_name = data.get("state")

    if not city_name or not state_name:
        return jsonify({"error": "City and state are required"}), 400

    locations = load_locations()
    if any(loc['city'].lower() == city_name.lower() and loc['state'].lower() == state_name.lower() for loc in locations):
        return jsonify({"error": "Location already exists"}), 400

    locations.append({"city": city_name, "state": state_name})
    save_locations(locations)
    return jsonify({"message": f"Location '{city_name}, {state_name}' added."})


# Remove a location with password
@app.route('/remove_location', methods=['DELETE'])
def remove_location():
    admin_password = request.headers.get('Admin-Password')

    if admin_password != admin_pass:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    city_name = data.get("city")
    state_name = data.get("state")

    if not city_name or not state_name:
        return jsonify({"error": "City and state are required"}), 400

    locations = load_locations()
    location_to_remove = next((loc for loc in locations if loc['city'].lower() == city_name.lower() and loc['state'].lower() == state_name.lower()), None)

    if location_to_remove:
        locations.remove(location_to_remove)
        save_locations(locations)
        return jsonify({"message": f"Location '{city_name}, {state_name}' removed."})
    else:
        return jsonify({"error": "Location not found"}), 404


if __name__ == '__main__':
    app.run()