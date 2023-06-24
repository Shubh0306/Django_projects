import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


# Read data
def get_data(id= None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

# get_data()




# Post data

def post_data():
    data = {
        'name': 'Ravi',
        'roll': 108,
        'city': 'Dhanbad',
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

#  post_data()



# update Data

def update_data():
    data = {  
        'id': 2,
        'name': 'Jack',
        'city': 'Columbia'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

update_data()


# delete data

def delete_data():
    data = {  
        'id': 5
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()



     

