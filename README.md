# Command Line Interface Point of Sale System
---
## Table of contents
---
1. [Overview](#project-overview)
2. [Features](#features)
3. [Demo](demo)
4. [Setup](#setup)
5. [Author](#author)

## Project Overview
---
This project is a command line-driven point-of-sale system built with Python. It is a single-user application that centers around CRUD operations in customers, products, and purchase modules. The objectives of this project were to implement OOP language concepts, log/display responses and system output on the command line interface as well as to allow the user to navigate application functionalities of this application according to the selected choices. 

##  About Project
---

- Entry file: main.py
- Interface: dashboard.py
- Instance unique identifier(Key): ID 
- License: MIT

1. Customer Module
    This module provides options through the interface that enable the handling of CRUD operations in the customer instances of the type CustomerProfile class. In this section, the user is prompted to create a new customer account, view customer accounts, delete a customer account, and or update customer account records. Other customer query options are reading customer information by either ID or name, and customer account instance validation by implementing unit testing to check whether the instance of that class exists.
    Related data and information from this module are stored in and accessed from the customer.json file in the database folder.

    Format sample:
    ```
        [
            {
                "customer_id": "C0001",
                "customer_name": "Bold User",
                "location": "Nairobi, Kenya",
                "contact": "254"
            },
        ]
    ```
2. Product Module
    This feature allows selecting options to handle create, read, update and delete functionalities on a product instance of type ProductProfile class. Similar to the customer module, the user can perform adding products, view products by name or product id, update product information and delete product operations.
    Related data and information from this module are stored in and accessed from the product.json file in the database folder.

    Format sample:
    ```
        [
            {
                "product_id": "P0001",
                "product_name": "Great Product",
                "quantity": 20,
                "price": 50.28,
                "description": "Tell something nice about the product"
            },
        ]
    ```
3. Purchases Module
    This module allows the user to make a purchase or view their purchase history. Upon customer validation, the user is prompted to select items to buy. Purchases can only be made of items available in stock, the user can either add a different item(s) to the cart or proceed to checkout. The receipts feature is nested as a submodule which enables printing out items bought and the total price. 

    A user purchase history is saved upon completion of each sales transaction to facilitate the view purchase history function.

    Related data and information from this module are stored in and accessed from the purchases.json and receipt.json files in the database folder.
### Features

1. Receipts. 
Upon each successful and complete purchase process, a sales receipt is printed out on the console showing transaction details.

### Technologies used
Language: Python version 3.8
IDE: pycharm, VSCode

### Project Illustrations
Project flow chart with [Miro](https://miro.com/app/board/uXjVPTFk5d4=/?share_link_id=89794991126) click to view.

## Setup
#### How to install this project:
    - Clone this repo, run:
        git clone https://github.com/John-Kimani/cli_POS_python.git
    - Move into the project folder:
        cd cli_POS_python
    - Open project with IDE i.e VsCode run:
        code .
    - Run entry file:
        python3 main.py

## Author
---
This project was developed by : [Kimani John](https://github.com/John-Kimani)