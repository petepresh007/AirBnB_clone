#!/usr/bin/python3
"""City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class
       Attributes:
       state_id: state.id
       name: name
    """
    state_id = ""
    name = ""
