import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog, QMenuBar, QMenu, QAction, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout

import csv

class Product:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        existing_product = next((p for p in self.products if p.id == product.id), None)
        if existing_product:
            print("ID already exists.")
        else:
            self.products.append(product)
            print("Product added successfully.")

    def remove_product(self, id):
        existing_product = next((p for p in self.products if p.id == id), None)
        if existing_product:
            self.products.remove(existing_product)
            print("Product removed successfully.")
        else:
            print("ID does not exist.")

    def find_product(self, id):
        return next((p for p in self.products if p.id == id), None)

    def update_product(self, id, name, category, price, quantity):
        existing_product = self.find_product(id)
        if existing_product:
            existing_product.name = name
            existing_product.category = category
            existing_product.price = price
            existing_product.quantity = quantity
        else:
            print("ID does not exist.")

    def save_inventory_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for product in self.products:
                writer.writerow([product.id, product.name, product.category, product.price, product.quantity])

    def load_inventory_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    id, name, category, price, quantity = row
                    product = Product(int(id), name, category, float(price), int(quantity))
                    self.products.append(product)
        except FileNotFoundError:
            print(f"Error: Could not open file {filename}")

class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management System")
        self.setGeometry(100, 100, 800, 600)

        self.inventory = Inventory()

        self.create_widgets()
        self.create_menus()

    def create_widgets(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        # Create tab for adding products
        add_product_tab = QWidget()
        self.tab_widget.addTab(add_product_tab, "Add Product")

        add_product_layout = QVBoxLayout()
        add_product_tab.setLayout(add_product_layout)

        form_layout = QFormLayout()
        add_product_layout.addLayout(form_layout)

        self.id_line_edit = QLineEdit()
        form_layout.addRow("ID:", self.id_line_edit)

        self.name_line_edit = QLineEdit()
        form_layout.addRow("Name:", self.name_line_edit)

        self.category_line_edit = QLineEdit()
        form_layout.addRow("Category:", self.category_line_edit)

        self.price_line_edit = QLineEdit()
        form_layout.addRow("Price:", self.price_line_edit)

        self.quantity_line_edit = QLineEdit()
        form_layout.addRow("Quantity:", self.quantity_line_edit)

        add_button = QPushButton("Add Product")
        add_button.clicked.connect(self.add_product)
        add_product_layout.addWidget(add_button)

        # Create tab for viewing products
        view_products_tab = QWidget()
        self.tab_widget.addTab(view_products_tab, "View Products")

        view_products_layout = QVBoxLayout()
        view_products_tab.setLayout(view_products_layout)

        search_layout = QHBoxLayout()
        view_products_layout.addLayout(search_layout)

        search_label = QLabel("Search:")
        search_layout.addWidget(search_label)

        self.search_line_edit = QLineEdit()
        search_layout.addWidget(self.search_line_edit)

        self.product_table = QTableWidget()
        self.product_table.setColumnCount(5)
        self.product_table.setHorizontalHeaderLabels(["ID", "Name", "Category", "Price", "Quantity"])
        view_products_layout.addWidget(self.product_table)

        buttons_layout = QHBoxLayout()
        view_products_layout.addLayout(buttons_layout)

        delete_button = QPushButton("Delete Product")
        delete_button.clicked.connect(self.delete_product)
        buttons_layout.addWidget(delete_button)

        update_button = QPushButton("Update Product")
        update_button.clicked.connect(self.update_product)
        buttons_layout.addWidget(update_button)

        # Create tab for file operations
        file_operations_tab = QWidget()
        self.tab_widget.addTab(file_operations_tab, "File Operations")

        file_operations_layout = QHBoxLayout()
        file_operations_tab.setLayout(file_operations_layout)

        save_button = QPushButton("Save Inventory")
        save_button.clicked.connect(self.save_inventory)
        file_operations_layout.addWidget(save_button)

        load_button = QPushButton("Load Inventory")
        load_button.clicked.connect(self.load_inventory)
        file_operations_layout.addWidget(load_button)

    def create_menus(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        help_menu = QMenu("Help", self)
        menu_bar.addMenu(help_menu)

        documentation_action = QAction("Documentation", self)
        documentation_action.triggered.connect(self.show_documentation)
        help_menu.addAction(documentation_action)

        support_action = QAction("Contact Support", self)
        support_action.triggered.connect(self.contact_support)
        help_menu.addAction(support_action)

        settings_menu = QMenu("Settings", self)
        menu_bar.addMenu(settings_menu)

        appearance_action = QAction("Appearance", self)
        appearance_action.triggered.connect(self.change_appearance)
        settings_menu.addAction(appearance_action)

    def add_product(self):
        try:
            id = int(self.id_line_edit.text())
            name = self.name_line_edit.text()
            category = self.category_line_edit.text()
            price = float(self.price_line_edit.text())
            quantity = int(self.quantity_line_edit.text())
            product = Product(id, name, category, price, quantity)
            self.inventory.add_product(product)
            self.populate_product_table()
            self.clear_line_edits()
        except ValueError:
            print("Invalid input. Please enter valid values.")

    def populate_product_table(self):
        self.product_table.setRowCount(len(self.inventory.products))
        for row, product in enumerate(self.inventory.products):
            self.product_table.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.product_table.setItem(row, 1, QTableWidgetItem(product.name))
            self.product_table.setItem(row, 2, QTableWidgetItem(product.category))
            self.product_table.setItem(row, 3, QTableWidgetItem(str(product.price)))
            self.product_table.setItem(row, 4, QTableWidgetItem(str(product.quantity)))

    def clear_line_edits(self):
        self.id_line_edit.clear()
        self.name_line_edit.clear()
        self.category_line_edit.clear()
        self.price_line_edit.clear()
        self.quantity_line_edit.clear()

    def delete_product(self):
        selected_items = self.product_table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select a product to delete.")
            return
        id = int(selected_items[0].text())
        self.inventory.remove_product(id)
        self.populate_product_table()

    def update_product(self):
        selected_items = self.product_table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select a product to update.")
            return
        id = int(selected_items[0].text())
        name = selected_items[1].text()
        category = selected_items[2].text()
        price = float(selected_items[3].text())
        quantity = int(selected_items[4].text())
        self.inventory.update_product(id, name, category, price, quantity)
        self.populate_product_table()

    def save_inventory(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Inventory", "", "CSV Files (*.csv)")
        if filename:
            self.inventory.save_inventory_to_file(filename)

    def load_inventory(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Inventory", "", "CSV Files (*.csv)")
        if filename:
            try:
                self.inventory.load_inventory_from_file(filename)
                self.populate_product_table()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file {filename}: {str(e)}")

    def show_documentation(self):
        print("Show documentation")

    def contact_support(self):
        print("Contact support")

    def change_appearance(self):
        print("Change appearance")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    inventory_app = InventoryApp()
    inventory_app.show()
    sys.exit(app.exec_())
