#Serialization Examples
#With pickle

import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickled_string)
print(pickle.loads(pickled_string))


#with json note you need to run
#easy_install simplejson before you have the proper libraries.
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
print(json.loads(json_string))


#using the file io operations you could save the state of your objects using this techniques. they work on objects
