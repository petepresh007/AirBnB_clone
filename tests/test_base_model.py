#!/usr/bin/python3
from models.base_model import BaseModel

model = BaseModel()
model.name = "My First Model"
model.my_number = 89
print(model)
model.save()
print(model)
model_json = my_model.to_dict()
print(model_json)
print("JSON of my_model:")
for k in model_json.keys():
    print("\t{}: ({}) - {}".format(k, type(model_json[k]), model_json[k]))
