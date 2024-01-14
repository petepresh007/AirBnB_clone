#!/usr/bin/python3
from models.base_model import BaseModel

model = BaseModel()
model.name = "My_First_Model"
model.my_number = 89
print(model.id)
print(model)
print(type(model.created_at))
print("--")
model_json = model.to_dict()
print(model_json)
print("JSON of my_model:")
for k in model_json.keys():
    print("\t{}: ({}) - {}".format(k, type(model_json[k]), my_model_json[k]))

print("--")
my_new_model = BaseModel(**model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
