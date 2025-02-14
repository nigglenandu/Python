#JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.


#Importing the JSON Module
import json


#Converting Python to JSON
#Use json.dumps() to convert a Python object to a JSON string.
python_obj = {"name": "Niggle", "age": 21}
json_str = json.dumps(python_obj)
print(json_str)  # Output: {"name": "Niggle", "age": 21}


#Converting JSON to Python
#Use json.loads() to convert a JSON string to a Python object.
json_str = '{"name": "Niggle", "age": 21}'
python_obj = json.loads(json_str)
print(python_obj)  # Output: {'name': 'Niggle', 'age': 21}

#Writing JSON to a File
#Use json.dump() to write a Python object to a JSON file.
with open("data.json", "w") as json_file:
    json.dump(python_obj, json_file)


#Reading JSON from a File
#Use json.load() to read a JSON file and convert it to a Python object.
with open("data.json", "r") as json_file:
    python_obj = json.load(json_file)
    print(python_obj)  # Output: {'name': 'Niggle', 'age': 251}


#Pretty Printing JSON
#Use json.dumps() with the indent parameter to pretty-print JSON.
json_str = json.dumps(python_obj, indent=4)
print(json_str)


#Sorting JSON Keys
#Use json.dumps() with the sort_keys parameter to sort the keys in the output.
json_str = json.dumps(python_obj, sort_keys=True)
print(json_str)  # Output: {"age": 21, "name": "Niggle"}