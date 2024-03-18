Inventory Management System
==========================

The Inventory Management System is a desktop application that allows users to manage their inventory of products. The application provides functionality for adding, updating, and removing products, as well as viewing the current inventory and saving/loading it to/from a file.

Features
--------

* Add products to the inventory with unique IDs, names, categories, prices, and quantities
* Update product information, including name, category, price, and quantity
* Remove products from the inventory by ID
* View the current inventory in a table, with columns for ID, name, category, price, and quantity
* Save the inventory to a CSV file for backup or sharing
* Load the inventory from a CSV file to restore or import data
* Customizable appearance with light and dark modes
* Criticality-based highlighting of product rows in the inventory table, based on the quantity in stock

Requirements
------------

* Python 3.x
* PyQt5

Installation
------------

1. Clone the repository to your local machine.
2. Install PyQt5 using `pip install PyQt5`.
3. Run the `main.py` file to launch the application.

Usage
-----

### Adding Products

1. Navigate to the "Add Product" tab.
2. Enter the product ID, name, category, price, and quantity in the corresponding fields.
3. Click the "Add Product" button to add the product to the inventory.

### Updating Products

1. Navigate to the "View Products" tab.
2. Select the product you want to update in the table.
3. Click the "Update Product" button to open the update dialog.
4. Modify the product information as desired.
5. Click the "Update" button to save the changes.

### Removing Products

1. Navigate to the "View Products" tab.
2. Select the product you want to remove in the table.
3. Click the "Remove Product" button to remove the product from the inventory.

### Saving the Inventory

1. Navigate to the "File Operations" tab.
2. Click the "Save Inventory" button to open the save dialog.
3. Choose a location and file name for the CSV file.
4. Click the "Save" button to save the inventory to the file.

### Loading the Inventory

1. Navigate to the "File Operations" tab.
2. Click the "Load Inventory" button to open the open dialog.
3. Choose a CSV file to load.
4. Click the "Open" button to load the inventory from the file.

### Changing the Appearance

1. Navigate to the "Settings" menu.
2. Choose either "Light Mode" or "Dark Mode" to change the appearance of the application.

License
-------

The Inventory Management System is licensed under the [Apache License, Version 2.0](LICENSE).
