# **Location App Microservices to Search/Add/Remove Data**

This app is made using flask to manage your location dataset allowing you to: search, add locations and remove locations.

Note: Add and remove is only available to the admin for security.

## **Search Locations:**

Utilizing the GET method you can query the locations.json file by city to return matching city, state data. This will accept partial names and return ALL matching values.
URL: /search

Example call:
```curl "http://127.0.0.1:5000/search?query=Spring"```

Example return:

```
["Springfield, MA", "Springfield. IL"]
```

## **Add Locations:**

Utilizing the POST method you can add new locations manually to the locations.json file. This will need to conform to the City, State format. If you attempt to add data with the wrong
password, or dupe data of what is already there the equest will not go through.
URL: /add_location

Example call:
``` curl -X POST http://127.0.0.1:5000/add_location \
     -H "Content-Type: application/json" \
     -H "Admin-Password: aaaaaa" \
     -d '{"city": "Seattle", "state": "WA"}'
```
Example return:

```
{
  "message": "Location 'Seattle, WA' added."
}
```

## **Remove Locations:**

Utilizing the DELETE method you can remove locations manually from the locations.json file. This will need to conform to the City, State format. If you attempt to delete data with the wrong passowrd,
or data that is not there you will receive an error.
URL: /remove_location

Example call:
``` curl -X DELETE http://127.0.0.1:5000/remove_location \
     -H "Content-Type: application/json" \
     -H "Admin-Password: aaaaaa" \
     -d '{"city": "Seattle", "state": "WA"}'
```
Example return:

```
{
  "message": "Location 'Seattle, WA' removed."
}
```

To set your own admin passowrd please utilize the admin_pass variable, this sets the password which is then passed to the header for security. Your data is stored in the
locations.json file.

You can also utilize my test file and test via command line as shown in my video.

Note: Please install flask and requests packages if you do not have these. This is essential for the code to run.


### **Communication Contract:**

All messages will be replied to within 48 hours via my oregonstate email.

### **UML Diagram:**

![image](https://github.com/user-attachments/assets/954a186f-6df8-4f2b-9f97-919f02aef837)
