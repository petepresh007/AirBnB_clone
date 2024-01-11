# AirBnB Clone - The Console

## Project Description

This project is an AirBnB clone implemented in Python, featuring a command-line interface (CLI) for seamless interaction. The primary focus is on utilizing the cmd module and employing Object-Oriented Programming (OOP) principles. Data is stored using JSON, providing a flexible and easy-to-use platform for managing AirBnB-like entities.

## Command Interpreter Overview

The command interpreter serves as the gateway to interact with the AirBnB clone. It supports various commands, allowing users to perform operations like creating, updating, deleting, and querying data. The entire structure is designed with modularity and extensibility in mind, making it easy to add new features and functionalities.

## How to Start

To start the AirBnB clone console, follow these steps:

- Clone the repository to your local machine:
 git clone https://github.com/Ogechukwu11/AirBnB_clone.git

- Navigate to the project directory:
 cd airbnb-clone

- Launch the console:
 python3 console.py

## How to Use

Once the console is running, you can enter commands following the syntax:
 (command) (options)

Here are some essential commands:

- 'create': Create a new instance.
- 'show': Display information about a specific instance.
- 'update': Update attributes of an instance.
- 'destroy': Delete a specified instance.
- 'all': Display all instances or all instances of a specific class.
- 'quit' or 'EOF': Exit the console.

## Examples

- Creating a new user:
 (console) create User

- Updating the name of a place:
 (console) update Place 1234-1234-1234 name "New Name"

- Showing information about a specific booking:
 (console) show Booking 5678-5678-5678

Feel free to explore and experiment with various commands to make the most out of the AirBnB clone console!
