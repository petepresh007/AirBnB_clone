#!/usr/bin/python3
"""Module for users class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class
        attributes:
        email: user email
        password: user password
        first_name: user first name
        last_name: user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
